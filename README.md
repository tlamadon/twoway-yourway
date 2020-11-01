# twoway-yourway
Implement your own version of two way fixed effect estimators. This is meant as a learning tool!

We are starting this as an assignment in the labor course at UChicago. Anyone can submit code which computes a two way fixed effect decomposition when given as an input a csv file with 3 columns `i` the worker id, `fid` the firm identifier and `lw` the log wage. You can find an example of such a data file here [matched-data.csv](data/matched-data.csv).  

For now the data is guaranteed to be connected, so no need to compute the connected set. Just construct the firm fixed effects and return them as a dictionary into a `json` file as in [results.json](sample-python/results.json).

The code should be callable from the terminal. Iy can be written in any language, and we will figure out as we go how to guarantee that the required packages are available. We will probably rely on conda.

Create a folder with your name or pseudo or team name, add your code to it and add a `infos.json` file that contains the command that should be used for execution, see [infos.json](sample-python/infos.json). Then submit your code as a `pull request`. 

We will compile a leader board!

I have added a simple zig-zag example in the python-example folder.

Good luck!

