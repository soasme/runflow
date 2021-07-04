# Command-Line Interface (CLI)

## Run

Command `runflow run` runs a flow spec file.

Run a flow spec with a given path to a file.

```bash
$ runflow run /path/to/flow_spec.hcl
```

Run a flow spec with a given import string.

```bash
$ runflow run path.to.package.module.flow_spec:flow
```

Run with variables.

```bash
$ runflow run /path/to/flow_spec.hcl --var 'key=value' --var 'key2=value2'
```

Run with variable  files.

```bash
$ cat vars.hcl
key = "value"
key2 = "${ key }2"

$ runflow run /path/to/flow_spec.hcl --var-file vars.hcl
```

## Visualize

:::tip
This feature requires `pygraphviz`.

Install `graphviz`:
```bash
$ sudo apt-get install graphviz-dev # Debian/Ubuntu user.

$ sudo yum install graphviz-devel # RedHat/CentOS user.

$ brew install graphviz # Mac user.
```

Then, install `pygraphviz`:
```bash
$ pip install runflow[pygraphviz]
```
:::

Command `runflow visualize` generates a graph representation of a flow spec file.

Generate a PNG file.

```bash
$ runflow visualize /path/to/flow_spec.hcl --output visualize.png
$ open visualize.png
```

Generate an SVG file.

```bash
$ runflow visualize /path/to/flow_spec.hcl --output visualize.svg
$ cat visualize.svg
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="169pt" height="44pt"
... (truncated)
</svg>
```

Generate a DOT file.

```bash
$ runflow visualize /path/to/flow_spec.hcl --output visualize.svg
$ cat visualize.svg
strict digraph "" {
	graph [bb="0,0,161.19,36"];
	node [label="\N"];
	"task.bash_run.echo"	[height=0.5,
		pos="80.593,18",
		width=2.2387];
}
```
