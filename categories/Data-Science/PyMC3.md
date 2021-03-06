---
title: PyMC3 
author: Luke 
image: https://i.stack.imgur.com/iG6NM.png
description: Looking at this academically-focused, Bayesian-style Python data science library. 
topics: PyMC3 usage, the with keyword and it's relevance to PyMC3, model state
---

# [PyMC3](https://docs.pymc.io/notebooks/getting_started.html)

Here is a helpful notebook from a PyData talk from [Nicole Carlson.](../../MLProjects/Notes/Sci-Kit-Vs-PyMC3/Talk.ipynb)

## Usage

1. Parameterize
2. Inference
3. Interpret
4. Predict



## With 

`with` statements are used as **context managers**.  Pass a `pm.Model()` object to it and all variables and functions in the block are added to the model.

## State 

### Variables 

The variable names and the string passed to the prior distribution functions should be the same.  

```python
lambda_1 = pm.Exponential("lambda_1", alpha)
```




