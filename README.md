# Natural Language to SQL
This project will convert natural language given context around the data and generate a working SQL query.  

## Docs   
[Spec Document](doc-link)
[Scope Document](doc-link)

## Development Notes  
NL2SQL will follow a trunk-based development pattern where features are developed in short-lived feature branches and continuously integrated back into the main branch. See more info about trunk-based workflow [here](https://trunkbaseddevelopment.com/). **The main branch will act as the production branch.**   

### Local Development   
Download the software locally by running 
```console
git clone git@github.com:jayupad/NL2SQL.git  
```
#### Conda Virtual Environment
The python version used in development is 3.12. Then, navigate to the directory and create the conda env `nl2sql` environment through the following commands.  
```console
conda create -n nl2sql python=3.12
conda activate nl2sql
```
#### Pip Virtual Environment
Navigate to the directory and execute the following console commands.
```console
python3 -m venv nl2sql
source nl2sql/bin/activate
pip3 install -r requirements.txt
```

## Environment Variables   
To run scripts in this repository, you require the necessary environment variables. These variables can either
be in your `.bash_profile` or in a `.env` file created and stored in the base directory of this repository. The relevant values will be updated below as development continues. 

## Testing  
Execute unit tests from the main directory of this repository through the console using the following command:
```console   
make test-unit   
```

Integration tests can be executed using the following command:
```console   
make test-integration
```   

End to end tests can be executed using the following command:
```console   
make test-e2e
```