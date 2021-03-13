# pattern-language-graph
A graphml file (and associated generator) mapping the relationships between patterns in [A Pattern Language](https://en.wikipedia.org/wiki/A_Pattern_Language) by Christopher Alexander et al.

NOTE: The provided file is not perfect! The data is collected automatically, so there will be errors. If you need a perfect version of the graph, it will need to be manually corrected.

## Use

This project is meant to facilitate other people taking the data encoded in A Pattern Language and using it for research, or to create visualizations. As such the graph, as well as the python script for generating the graph are provided for free under the MIT License.

To run the script on your own version of A Pattern Language, you will need a .txt file version of the book. One option for accomplishing this is to find a PDF version of the book, and then run the PDF through a [PDF to .txt converter](https://document.online-convert.com/convert-to-txt). After that you can pass the name of your text file and output file to the script. For example:

```
python3.6 process.py a-pattern-language.txt pattern-graph.graphml
```

Depending on your text file, the script may not be able to identify the pattern headers, which allow it to process the file. In this case you can modify the script's regex to match the format of the headers in your file. The different stages of processing the input (eg identifying headers, removing page numbers, etc) are encapsulated in well-named functions, so modifying the script should be relatively simple =)

## File

Nodes in the graph represent patterns, which have different properties. These properties include:
  * id, the identifying number of the pattern.
  * name, the name of the pattern.
  * section, the larger section of the book the pattern belongs to (towns, buildings, or construction).
  * subsection, the smaller section the pattern belongs to. These names were decided by me based on the descriptions in the book.
  * stars, a number representing the number of stars the pattern was given by the authors.

The edges in the graph represent connections between patterns. All of the edges are directional, going from larger "parent" patterns to smaller "child" patterns. Every edge also has a property called "origin" which specifies whether the link was found at the beginning of a pattern (value "start")or at the end of a pattern (value "end").

## Feedback

If you do decide to use this for a project, please send me a link to it! I'd love to see what people come up with. You can email me at bekawestberg@gmail.com

## Contributing

If you find any errors in the graph please feel free to file an issue, or create a pull request fixing it! For pull requests, please make your modifications inside the process.py `postProcessGraph` function. Making your modifications there instead of directly modifying the file means that people who run the script themselves will also get your changes =)

