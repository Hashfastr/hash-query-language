import { useState, useEffect } from 'react';
import { api } from '../services/api';
import type { SchemaField } from '../types';

export function SchemaExplorer() {
  const [schema, setSchema] = useState<SchemaField[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedFields, setExpandedFields] = useState<Set<string>>(new Set());
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadSchema();
  }, []);

  const loadSchema = async () => {
    try {
      const data = await api.getSchema();
      setSchema(data);
      setError(null);
    } catch (err) {
      setError('Failed to load schema');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const toggleExpand = (fieldPath: string) => {
    setExpandedFields((prev) => {
      const next = new Set(prev);
      if (next.has(fieldPath)) {
        next.delete(fieldPath);
      } else {
        next.add(fieldPath);
      }
      return next;
    });
  };

  const filterFields = (fields: SchemaField[], search: string): SchemaField[] => {
    if (!search) return fields;

    return fields.filter((field) => {
      const matchesName = field.name.toLowerCase().includes(search.toLowerCase());
      const hasMatchingChildren = field.children && filterFields(field.children, search).length > 0;
      return matchesName || hasMatchingChildren;
    });
  };

  const renderField = (field: SchemaField, depth = 0, parentPath = '') => {
    const fieldPath = parentPath ? `${parentPath}.${field.name}` : field.name;
    const isExpanded = expandedFields.has(fieldPath);
    const hasChildren = field.children && field.children.length > 0;

    return (
      <div key={fieldPath}>
        <div
          className={`flex items-center gap-2 py-1 px-2 hover:bg-gruvbox-light-bg2 dark:hover:bg-gruvbox-dark-bg2 cursor-pointer rounded`}
          style={{ paddingLeft: `${depth * 1 + 0.5}rem` }}
          onClick={() => hasChildren && toggleExpand(fieldPath)}
        >
          {hasChildren && (
            <span className="text-xs">
              {isExpanded ? '▼' : '▶'}
            </span>
          )}
          {!hasChildren && <span className="text-xs opacity-0">◦</span>}
          <span className="font-medium">{field.name}</span>
          <span className="text-xs text-gruvbox-light-aqua dark:text-gruvbox-dark-aqua">
            {field.type}
          </span>
        </div>
        {hasChildren && isExpanded && (
          <div>
            {field.children!.map((child) => renderField(child, depth + 1, fieldPath))}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="sidebar w-64 flex flex-col h-full">
      <div className="p-4 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
        <h3 className="font-bold mb-3">Schema Explorer</h3>
        <input
          type="text"
          placeholder="Search fields..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="input w-full text-sm"
        />
      </div>

      <div className="flex-1 overflow-y-auto p-2">
        {loading && (
          <div className="text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray p-2">
            Loading schema...
          </div>
        )}

        {error && (
          <div className="text-sm text-gruvbox-light-red dark:text-gruvbox-dark-red p-2">
            {error}
            <button
              onClick={loadSchema}
              className="block mt-2 text-xs underline"
            >
              Retry
            </button>
          </div>
        )}

        {!loading && !error && schema.length === 0 && (
          <div className="text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray p-2">
            No schema available
          </div>
        )}

        {!loading && !error && schema.length > 0 && (
          <div className="space-y-1">
            {filterFields(schema, searchTerm).map((field) => renderField(field))}
          </div>
        )}
      </div>

      <div className="p-2 border-t border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2 text-xs text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
        {schema.length} fields
      </div>
    </div>
  );
}
