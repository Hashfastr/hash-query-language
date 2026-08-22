See @README.md for context to this project

Ensure imports are optimized, they should be Python 3.9 compatible.

Use TYPE_CHECKING from typing and forward references for all imports that are made solely for type annotation.

For imports ensure that large generic imports such as `import polars as pl` are avoided and replaced by narrowed imports.

When an import is only used for specific usecases, such as a call within a single class method, delay that import into that method.

GOAL: increase run times and speed of the program, this is crucial as this is meant to be used as a library and not just a singular program.
