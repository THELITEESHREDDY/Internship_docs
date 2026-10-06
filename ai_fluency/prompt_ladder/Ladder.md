# Task : Designing a backend

## prompt v1: write backend code for quiz app in fastapi

### What changed in the prompt.
### starting one, nothing here

### what actually improved in the output.
### a basic version with routes is done

### what still failed.
### lot of things, all the code is placed in single code block
### no separation of concerns, weak data models

### what you would try next. 
### first to re-write the code with seperating routes with bussiness logic as it is looking 
### messy 



## prompt v2: in the given code for each route make a separate controller that handles the business logic
## making routing and logic separate

### What changed in the prompt.
### instructing to write code in seperated blocks that sperates the messy code to different files

### what actually improved in the output.
### re-written version focusing on seperating routes with business logic 

### what still failed.
### still the code is little adjusted in the same files, as it changes only the requested area, not focused on 
### overall speration of concers

### what you would try next. 
### ask it to keep in mind of overall seperation of concerns for each part not only what i asked to do



## prompt v3: in the given code for each route make a separate controller that handles the business logic
## making routing and logic separate

### What changed in the prompt.
### instructing to write code in seperated blocks that sperates the messy code to different files

### what actually improved in the output.
### re-written version focusing on seperating routes with business logic 

### what still failed.
### still the code is little adjusted in the same files, as it changes only the requested area, not focused on 
### overall speration of concers

### what you would try next. 
### ask it to keep in mind of overall seperation of concerns for each part not only what i asked to do


## prompt v4: this is not only limited to routes and controllers, re-write the code by separating the independent parts in the whole applicaion like db, config, routes, controllers, main.py

### What changed in the prompt.
### this time i asked it to make the project by divinding the work across seperate files

### what actually improved in the output.
### this time i received each seperate code for individual task that it does, routes one place, controllers, config etc

### what still failed.
### For a project we need the architecture and design through which we want to build, that is missing

### what you would try next. 
### I try to ask it to design first then based on the design i'll ask to build the files seperately 


## prompt v5: We are good for now, but any project starts with design, so first lets write the design then see the project structure, and build accordingly


### What changed in the prompt.
### i prompted it to make the project by first designing, later to work

### what actually improved in the output.
### It literally suggested me the flow of design and based on that it recommended some entities, use cases, requirments, api design, applicaiton flow etc

### what still failed.
### still there are some gaps in the way the design works

### what you would try next. 
### this time i try to give full design by filling the gaps, that it has shown me, may be this will be the a file, lets see how it works


## prompt v5: We are good for now, but any project starts with design, so first lets write the design then see the project structure, and build accordingly


### What changed in the prompt.
### i prompted it to make the project by first designing, later to work

### what actually improved in the output.
### It literally suggested me the flow of design and based on that it recommended some entities, use cases, requirments, api design, applicaiton flow etc

### what still failed.
### still there are some gaps in the way the design works

### what you would try next. 
### this time i try to give full design by filling the gaps, that it has shown me, may be this will be the a file, lets see how it works






## prompt v6: I want to build a software project, but before writing any code, I want you to design the system properly. Act as a senior software architect and product designer first, not as a programmer. Your job is to understand the problem, clarify the product goal, identify the users and their needs, and turn those requirements into a practical technical design.

Start by defining the problem the application solves, its purpose, target users, major actors, core user journeys, functional requirements, non-functional requirements, and the scope of the first version. Clearly separate essential V1 functionality from features that should be postponed. If any requirement is unclear, make a reasonable assumption and explicitly state it rather than silently guessing.

Then design the domain. Identify the important entities, their responsibilities, relationships, ownership, lifecycle, and business rules. Determine what data the system needs to store and how that data should be represented in a relational database. Define tables, important fields, relationships, constraints, and indexing considerations while avoiding unnecessary complexity.

Next, design the API around the actual use cases rather than around database tables. Define the major endpoints, HTTP methods, request and response contracts, authentication and authorization requirements, validation rules, and expected error behavior. Explain important flows such as registration, authentication, creation, updates, and the primary user operation from request to database and back.

After the domain and API are clear, design the application architecture. Establish clear boundaries between HTTP/API handling, controllers or request coordination, business services, repositories/database access, models, schemas, configuration, authentication, exceptions, and infrastructure. Every layer should have a specific responsibility, and business logic should not be scattered across routes or database code. Explain dependency direction and how the major components communicate.

Also consider security, data integrity, transactions, concurrency, logging, observability, testing, configuration management, migrations, deployment, and future scalability. Do not overengineer the first version, but ensure the design can evolve without requiring a complete rewrite.

Only after the design is complete should you derive the project structure. Explain why each major directory and file exists and map it back to the architectural responsibilities.

For important architectural decisions, explain the reasoning, alternatives, and tradeoffs. Challenge weak assumptions and point out potential design problems.

Do not write implementation code yet. First produce a complete design specification that I can review and approve. Once the design is finalized, we will derive the project structure and implement the system step by step.

The goal is not simply to make the application work. The goal is to design a maintainable, testable, secure, understandable, and production-oriented system whose architecture is justified by the requirements.


### What changed in the prompt.
### it is more detailed for the design 

### what actually improved in the output.
### design requirements are really went well and the work was really good

### what still failed.
### i think, this time it did the best 

### what you would try next. 
### ask it to build!!!