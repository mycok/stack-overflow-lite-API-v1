[![Build Status](https://travis-ci.org/mkibuuka/stack-overflow-lite-API-v1.svg?branch=fetch_all_answers)](https://travis-ci.org/mkibuuka/stack-overflow-lite-API-v1) [![Coverage Status](https://coveralls.io/repos/github/mkibuuka/stack-overflow-lite-API-v1/badge.svg?branch=fetch_all_answers)](https://coveralls.io/github/mkibuuka/stack-overflow-lite-API-v1?branch=fetch_all_answers) [![Maintainability](https://api.codeclimate.com/v1/badges/b411231596221ef4bbb3/maintainability)](https://codeclimate.com/github/mkibuuka/stack-overflow-lite-API-v1/maintainability)

## Stack-Overflow-Lite-API-v1
Stack-overflow-lite is a blog web application that facilitates people interaction by providing an interface for submitting questions and answers about any topic/issue that anyone feels like addressing.

### This repo includes stack-overflow-lite source code files for:
* Endpoints
* Unittests
* Flask
* Question Models
* Answer Models


## Question Models:
These represent a question that could be posted by a user on the app platform. The question object takes three required attributes (title, body, tag).
A **url** to post a question could take a **POST** request to an endpoint with a format such as **api/v1/questions**.

A user question could be formatted and posted as below:
```json
{
	"title": "Git branching ",
	"body": "What does it mean to create a separate branch for every feature while implementing a series of tasks using git?",
	"tag": "Version Control"
}
```
And the response could be as below:
```json
{
    "answers": [],
    "body": "What does it mean to create a separate branch for every feature while implementing a series of tasks using git?",
    "date_posted": "Sat, 18 Aug 2018 15:49:19 GMT",
    "id": 1,
    "status": "success",
    "tag": "Version Control",
    "title": "Git branching ",
    "status": "success"
}
```
A **url** to fetch a single question by **id** could take a **GET** request to an endpoint with a format such as **api/v1/questions/id** and the response could be formatted as below:
```json
{
    "answers": [],
    "body": "What does it mean to create a separate branch for every feature while implementing a series of tasks using git?",
    "date_posted": "Sat, 18 Aug 2018 15:49:19 GMT",
    "id": 1,
    "status": "success",
    "tag": "Version Control",
    "title": "Git branching ",
    "status": "success"
}
```
A **url** to fetch all questions could take a **GET** request to an endpoint with a format such as **api/v1/questions** and the response could be formatted as below:
```json
{
	"questions": [
        {
            "answers": [
                {
                    "body": "branching means creating a copy of your existing work and transffering it to another container where you intend to add more features to it without compromising your old features",
                    "date_posted": "Sat, 18 Aug 2018 16:03:06 GMT",
                    "id": 1
                }
            ],
            "body": "What does it mean to create a separate branch for every feature while implementing a series of tasks using git?",
            "date_posted": "Sat, 18 Aug 2018 15:49:19 GMT",
            "id": 1,
            "tag": "Version Control",
            "title": "Git branching "
        },
        {
            "answers": [],
            "body": "Does anyone else think the term FUN is overrated?, Is it possible to have FUN by actually not having fun? ",
            "date_posted": "Sat, 18 Aug 2018 16:28:26 GMT",
            "id": 2,
            "tag": "Life",
            "title": "Fun"
        }
    ],
    "status": "success"
}
```

## Answer Models:
These represent an answer that could be posted by a user on the app platform. Every answer is mapped to a specific question by a unique question **id** that's assigned through a **url** such as **api/v1/questions/1/answers**.
A user answer could be formatted and posted as below:
```json
{
	    "body": "branching means creating a copy of your existing work and transffering
               it to another container where you intend to add more features to it without
               compromising your old features"
}
```
And the response will be as below:
```json
{

    "answers": [
        {
            "body": "branching means creating a copy of your existing work and transffering
                     it to another container where you intend to add more features to it 
                     without compromising your old features",
                     
            "date_posted": "Sat, 18 Aug 2018 16:03:06 GMT",
            "id": 1
        }
    ],
    
    "body": "What does it mean to create a separate branch for every feature while
             implementing a series of tasks using git?",
             
    "date_posted": "Sat, 18 Aug 2018 15:49:19 GMT",
    "id": 1,
    "status": "success",
    "tag": "Version Control",
    "title": "Git branching ",
    "status": "success"
}
```


