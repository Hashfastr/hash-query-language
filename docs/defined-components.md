# Functions and definitions

## Field name aliases
```
T
| where nasty.field.naming_ip == "127.0.0.1"

let ip = nasty.field.naming_ip;
T
| where ip == "127.0.0.1"
```

Do we just mass import this then? What about nested-ness

```
// empty object
let ip = object();
let ip.src = nasty.src.field.naming_ip;
let ip.dest = nasty.dest.field.naming_ip;
T
| where ip.src == "127.0.0.1" and ip.dest == "1.3.3.7"
```

Better way?

```
let ip = {
    "src": nasty.src.field.naming_ip,
    "dest": nasty.dest.field.naming_ip,
}
```

Don't really like it, it's like writing json not Hql.
But it's nicer than how kusto actually does it.

## Configuring mappings
Configuration definition that would look like this:

```yml
mapping:
  name: 'T ip mapping'
  pattern: 'network-2022-*'
  mappings:
    ip.src: nasty.src.field.naming_ip
    ip.dest: nasty.dest.field.naming_ip
    timestamp: "['@timestamp']"
```

Mapping source names are simple paths that can be split on the dot.
Don't expect

```
ip.domain.com.owner -> ['ip', 'domain.com', 'owner']
```

will be

```
ip.domain.com.owner -> ['ip', 'domain', 'com', 'owner']
```

Maybe put hql into the config and parse it to allow for this?
