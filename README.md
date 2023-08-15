# Test Inficial

Infisical is an open-source, end-to-end encrypted secret management platform that enables teams to easily manage and sync their environment variables.
In infisical can using client or CLI.

### First Install CLI 
[This Instalation Inficial] (https://infisical.com/docs/cli/overview)

### Next, Login Account Infisical

In login, you can use:

```
 infisical login
```
Next, input the domain, if you using a local server you can input like this: 

```
v Override current logged in user       
v Self Hosting
x Domain: http://192.168.0.0:9862
```

and next input email and password. You are login using you're account now

### Initialize a project

Infisical must initialize a project before start using environment inside your project directory. You can type: 

```
infisical init
```
Then select a project environment from Inficial. (You can add this from a UI Infisical)
After initialize complete, in your project will have a file <b>.infisical.json</b>

### Running a project using infisical

For running a project, must using infisical first like: 
```
infisical run --env=dev --path=/ -- python main.py   
```
Then wala :sparkles: you can running a code without .env in your project
