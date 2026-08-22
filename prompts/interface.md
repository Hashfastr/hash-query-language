See @README.md for context.
Always use uv for package management, venv is at @.venv
Instructions for the grammar is at @Hql/Parser/grammar/README.md

I need to replace the existing web interface in @Hql-Interface with something new and better.

The web interface should mimic a SIEM with multiline input, similar to Azure Data Explorer. It should have syntax checking and auto complete using the grammar files @Hql/Parser/grammar/Hql.g4 and @Hql/Parser/grammar/HqlTokens.g4

It will interface with a backend with an API that is currently defined in @Hql/Apiserver. The website should be light.

More details on the web interface are as follows:

- Multiline text box taking most of the interface.
  - Row above should have
    - Run button, stop button
    - Tabs for multiple queries
- A list on the right showing existing detections
    - Should be collapsible
- A run buttom and stop button in a row on the top of the text box.
    - Stop button might not have functionality yet.
- When running a query
    - Show a gif next to the run button, this gif is contained here: @Hql-Interface/lain.gif
    - Cannot start another query while waiting for one to finish
- When displaying results
    - Rows shown for each table should give a header line with names of the columns
    - Each table has a tab for the results to represent different datasets.
    - Can expand rows
        - Replaces right side content until closed
        - Shows a beautified json representation of the row
    - Nested data in any given cell should be shown as a truncated collapsed json representation
    - Should nested data exist but it only has one endpoint, e.g. objects containing single objects containing single elements, the name in the header should be expanded to just a dot separated path.
    - User can right click a cell and copy the value of the cell directly
- Minimal complexity, can be easily contained in behavior
    - No complex dependencies
    - No scaling
    - Can be easily run on a laptop.
- Dark and light mode toggle

Since this is a toy interface, and the api server does not have it, don't implement authentication.
Let's save that for dedicated session that I can audit.
