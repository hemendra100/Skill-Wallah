#!/usr/bin/env python
# coding: utf-8

#  What is the Probability density function

# The Probability Density Function (PDF) is a fundamental concept in probability theory and statistics. It is a function that describes the likelihood of a continuous random variable taking on a specific value or falling within a certain range of values. 

# What are the types of Probability distribution

# Discrete Probability Distribution:
# Discrete probability distributions are used for random variables with countable outcomes, where the values can only take specific, distinct values. The probability of each possible outcome is explicitly defined.
# 
# Examples of discrete probability distributions:
# 
# Bernoulli Distribution: A simple binary distribution with two outcomes (success and failure) with a fixed probability of success.
# Binomial Distribution: Describes the number of successes in a fixed number of independent Bernoulli trials.
# Poisson Distribution: Models the number of events that occur in a fixed interval of time or space.
# Continuous Probability Distribution:
# Continuous probability distributions are used for random variables with continuous outcomes, where the values can take any value within a given range. The probability of any specific value is typically zero, and probabilities are defined over intervals.
# 
# Examples of continuous probability distributions:
# 
# Normal Distribution (Gaussian Distribution): A symmetrical bell-shaped distribution widely used due to the Central Limit Theorem. Many natural phenomena follow approximately normal distributions.
# Uniform Distribution: Represents constant probability over a continuous interval, where all values within the interval have the same probability.
# Exponential Distribution: Models the time between events in a Poisson process, such as the time between arrivals of customers in a queue.

#  Write a Python function to calculate the probability density function of a normal distribution with 
# given mean and standard deviation at a given point.

# In[5]:


from scipy.stats import norm

def normal_pdf(x, mean, std_dev):
    """
    Calculate the Probability Density Function (PDF) of a normal distribution
    at a given point.

    Parameters:
        x (float): The point at which to calculate the PDF.
        mean (float): Mean (average) of the normal distribution.
        std_dev (float): Standard deviation of the normal distribution.

    Returns:
        float: The PDF value at the given point.
    """
    pdf_value = norm.pdf(x, loc=mean, scale=std_dev)
    return pdf_value

# Example usage:
mean = 0
std_dev = 1
x_value = 1.5
pdf_at_x = normal_pdf(x_value, mean, std_dev)
print(f"PDF at x={x_value}: {pdf_at_x}")


# The Binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, where each trial has only two possible outcomes: success (S) or failure (F). The Binomial distribution has the following properties:
# 
# Fixed Number of Trials: The number of trials, denoted by "n," is fixed and known in advance.
# 
# Independent Trials: Each trial is independent of the others, meaning the outcome of one trial does not influence the outcomes of the other trials.
# 
# Constant Probability of Success: The probability of success, denoted by "p," remains constant for each trial. Similarly, the probability of failure is "1 - p."
# 
# Discrete Outcomes: The random variable "X" representing the number of successes takes on discrete values, starting from 0 up to "n."

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters for the binomial distribution
sample_size = 1000
probability_success = 0.4

# Generate a random sample from the binomial distribution
random_sample = np.random.binomial(n=1, p=probability_success, size=sample_size)

# Plot a histogram of the results
plt.hist(random_sample, bins=2, edgecolor='black', alpha=0.7)
plt.xticks([0, 1], ['Failure', 'Success'])
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Histogram of Random Sample from Binomial Distribution')
plt.show()


# In[7]:


pip install scipy


# In[8]:


from scipy.stats import poisson

def poisson_cdf(x, mean):
    """
    Calculate the Cumulative Distribution Function (CDF) of a Poisson distribution
    at a given point.

    Parameters:
        x (int): The point at which to calculate the CDF.
        mean (float): Mean of the Poisson distribution.

    Returns:
        float: The CDF value at the given point.
    """
    cdf_value = poisson.cdf(x, mu=mean)
    return cdf_value

# Example usage:
mean = 2.5
x_value = 4
cdf_at_x = poisson_cdf(x_value, mean)
print(f"CDF at x={x_value}: {cdf_at_x}")


# Binomial distribution is based on discrete events, while Poisson distribution is based on continuous events.
# Binomial distribution has a fixed number of trials, while Poisson distribution can have any number of events that occur during a certain time interval.
# Binomial distribution is biparametric, while Poisson distribution is uniparametric.
# Binomial distribution is characterized by two parameters n and p, while Poisson distribution is characterized by a single parameter m.

#  Generate a random sample of size 1000 from a Poisson distribution with mean 5 and calculate the 
# sample mean and variance.

# In[9]:


import numpy as np

# Parameters for the Poisson distribution
sample_size = 1000
mean = 5

# Generate a random sample from the Poisson distribution
random_sample = np.random.poisson(lam=mean, size=sample_size)

# Calculate the sample mean and variance
sample_mean = np.mean(random_sample)
sample_variance = np.var(random_sample, ddof=1)  # Using ddof=1 for sample variance

print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_variance)


#  How mean and variance are related in Binomial distribution and Poisson distribution

# Binomial Distribution:
# 
# In a Binomial distribution with parameters "n" (number of trials) and "p" (probability of success in each trial), the mean (μ) and variance (σ^2) are related as follows:
# 
# Mean (μ) = n * p
# Variance (σ^2) = n * p * (1 - p)

# Poisson Distribution:
# 
# In a Poisson distribution with parameter "λ" (the average rate of events occurring per unit of time or space), the mean (μ) and variance (σ^2) are related as follows:
# 
# Mean (μ) = λ
# Variance (σ^2) = λ

# the least frequent data appears at the tails or extreme ends of the distribution. The tails of the normal distribution represent the values that are farthest away from the mean.
# 
# The normal distribution is a bell-shaped curve, and its properties are such that:
# 
# The mean, median, and mode are all equal and located at the center of the distribution.
# 
# As you move away from the mean towards the tails, the data becomes less frequent.
# 
# The tails of the normal distribution extend to infinity on both sides but asymptotically approach the x-axis.
# 
# Therefore, the least frequent data appears in the tails of the normal distribution, farthest away from the mean. The data becomes rarer as it moves further from the center of the distribution. Conversely, the most frequent data is clustered around the mean, as it represents the central tendency of the data.
# 
# 
# 
# 
# 
# 

# In[ ]:




