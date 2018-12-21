# Log Analysis Project
Building a reporting tool that summarizes data from a large database

## Introduction
this project aims to explore a large database with over a million rows, then build and refine complex queries and use them to draw business conclusions from data.

The database includes three tables:
* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

## Running code
follow these steps:
1. Download the file `newsdata.sql` then load the data into local database using the command:
```
psql -d news -f newsdata.sql
```
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

2. Run the code using:
```
python LogAnalysis.py
```

## License

Copyright (c) 2018 Zeina Kittaneh

This project was submitted by Zeina Kittaneh as part of the Nanodegree At Udacity.

As part of Udacity Honor code, your submissions must be your own work, hence
submitting this project as yours will cause you to break the Udacity Honor Code
and the suspension of your account. Me, the author of the project, allow you to check the code as a reference.

Besides the above notice, the following license applies.

#### MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.