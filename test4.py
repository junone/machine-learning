import math
import pandas as pd
import numpy as np
from scipy import stats
#prob = stats.norm.pdf(x, mu, sigma)
#import matpltplot
 
boys = np.loadtxt('boy.txt')
boys = pd.DataFrame(boys)
girls = np.loadtxt('girl.txt')
girls = pd.DataFrame(girls)
boytest = np.loadtxt('boy82.txt')
boytest = pd.DataFrame(boytest)
print(boytest[0])
print(boytest[1])
print(boytest[2])


def stcboy():
    boysheight = boys[0]
    boysweight = boys[1]
    boysshoes = boys[2]
    boyHvar = np.var(boysheight)
    boyHmean = np.mean(boysheight)
    boyWvar = np.var(boysweight)
    boyWmean = np.mean(boysweight)
    boySvar = np.var(boysshoes)
    boySmean = np.mean(boysshoes)
    return(boyHvar, boyHmean, boyWvar, boyWmean, boySvar, boySmean)


def stcgirl():
    girlsheight = girls[0]
    girlsweight = girls[1]
    girlsshoes = girls[2]
    girlHvar = np.var(girlsheight)
    girlHmean = np.mean(girlsheight)
    girlWvar = np.var(girlsweight)
    girlWmean = np.mean(girlsweight)
    girlSvar = np.var(girlsshoes)
    girlSmean = np.mean(girlsshoes)
    return(girlHvar, girlHmean, girlWvar, girlWmean, girlSvar, girlSmean)

# def pretect():


def pretect(a, b, c, d, e, f, a1, b1, c1, d1, e1, f1):
	sum0=0
	sum1=0
	for i in range(82):
		height = boytest.iloc[i, 0]
		bph = stats.norm.pdf(height, b, a)
		weight = boytest.iloc[i, 1]
		bpw = stats.norm.pdf(weight, d, c)
		shoes = boytest.iloc[i, 2]
		bps = stats.norm.pdf(shoes, f, e)
		bpall = bph*bpw*bps
		height = boytest.iloc[i, 0]
		gph = stats.norm.pdf(height, b1, a1)
		weight = boytest.iloc[i, 1]
		gpw = stats.norm.pdf(weight, d1, c1)
		shoes = boytest.iloc[i, 2]
		gps = stats.norm.pdf(shoes, f1, e1)
		gpall = gph*gpw*gps
		print("bp,gp",bpall,gpall)
		if bpall > gpall:
			sum1 = sum1+1
		else:
			sum0 = sum0+1
	return(sum1/(sum0+sum1))
# print(height)


if __name__ == '__main__':
    a, b, c, d, e, f = stcboy()
    a1, b1, c1, d1, e1, f1 = stcgirl()
#	prob = stats.norm.pdf(x, mu, sigma)#正太分布函数值
    P = pretect(a, b, c, d, e, f, a1, b1, c1, d1, e1, f1)
    print(P)


# boysheight=boys[0]
# print(boysheight)
# sumheight=0
# dec=boys.describe()
# print(dec)
# print(np.var(boys))
