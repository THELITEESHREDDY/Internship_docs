# voice Card
I'm a backend engineer for autonomous AI agents. If you're a CTO shipping one to real users, 
I can own the parts that break: orchestration, state, concurrency, recovery, and observability.

Contact: Let's talk? 
Mail me at liteeshreddyofficial@gmail.com 


# Research agent

# The problem

Research takes me a lot of time. I had seen multi-agent systems, a technology that genuinely solves this problem. So I built one.

# What I did and decided

I built a multi-agent research engine. You give it a big topic, like a business, and it does the background research. An orchestrator agent reads the scope and requirements and splits the topic into angles. Each angle goes to its own agent: one on capital, one on raw material, one on transport and suppliers, one on marketing.

I first set a fixed maximum number of agents. Then I made it dynamic. A small topic needs fewer agents. A bigger one needs more, so each angle gets proper depth. Now the orchestrator decides how many to spin up.

# What came of it

I ran it on the requirement estimates for building an apartment. It used about 4 agents and took 3-4 minutes. By my estimate, doing it myself would take 3-4 hours. On other topics it used fewer agents or more, and the work still got done.


Next time: I wouldn't rebuild it. I'd put a more reliable, production-grade design on top, one that handles failures.