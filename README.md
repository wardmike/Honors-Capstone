# Pairs Trading for Cryptocurrencies
Honors Capstone for Michael Ward.  
Utah State University -- May 2018.

To run, clone the repo and make sure you have **Tkinter** and **Matplotlib** installed.  
Then, run **python3 main.py** to run the GUI.  
If you have any issues, feel free to email me at mikethebroski@gmail.com.

## Fundamental Goal
To learn algorithmic trading by creating and testing various algorithms with live market prices.

## Algorithms
### <a href="/Pairs/">Pairs Trading</a>
Finding the relationship between two or more prices.

### <a href="/Moving Averages/">Moving Averages</a>
Algorithms using the moving averages of the stock price over multiple days.

### <a href="/Mean Reversion/">Mean Reversion</a>
Improvement on Moving Averages where algorithms will place limits above and below the moving average.  
This will allow buy and sell times to more closely approach the highs and lows.

### Dynamic Mean Reversion
Improvement on Mean Reversion algorithm. Algorithm will dynamically change limits in accordance with stock's volatility.

## Results

### Moving Average Crossover on Bitcoin
With an initial investment of one Bitcoin and tested over a year and trading a maximum of once a day, the algorithm returned:  
Total Profit:  $1,894.86  
Percent Return:  311.3%  
Percent Return (buying and holding):  659.1%  

With an initial investment of one Bitcoin and tested from October 5 to November 3 and trading a maximum of once every 5 minutes, the algorithm returned:  
Total Profit:  $6,150.09  
Percent Return:  163.9%  
Percent Return (buying and holding):  142.3%  

\*\*While both algorithms returned less than buying and holding, moving average crossover may be more protected in case of a market crash. Further research will follow.

## Tasks

### Research
- [x] Write my first algorithm
- [ ] Learn how the stock market works: optimal times to buy and sell and how to best predict future changes.
- [ ] Learn the basics of algorithmic trading.

### Data Setup
- [x] Get past data
- [ ] plan to organize data
- [ ] sub-repo or regular data files?
- [ ] Create an account on QuantConnect and try trading

### Pairs Trading
- [ ] Dickey-Fuller algo in Python  
- [ ] Johansen cointegration test in Python (on Quantopian)  

### Moving Average Crossover
- [ ] Learn Moving Averages Crossover strategy.
- [ ] Test Moving Averages Crossover strategy with Bitcoin.
- [ ] Modify MVA test with Bitcoin to find better results.

### Writeup
- [ ] First Thesis Draft.
- [ ] Second Thesis Draft.
- [ ] Penultimate Thesis Draft
- [ ] Final Thesis Submission
- [ ] Present Thesis at Research Symposium

## Timeline

<table>
  <tr>
    <td>04/01/2018</td>
    <td>Penultimate Draft Submission</td>
  </tr>
  <tr>
    <td>05/01/2018</td>
    <td>Final Thesis Submission</td>
  </tr>
</table>

## Meetings

<table>
  <tr>
    <td>07/20/2017</td>
    <td>Met with Prof. Brim to discuss Mean Reversion and Dynamic Mean Reversion strategies.</td>
  </tr>
  <tr>
    <td>09/11/2017</td>
    <td>Met with Prof. Brim to discuss Bitcoin strategies.</td>
  </tr>
  <tr>
    <td>09/18/2017</td>
    <td>Met with Prof. Brim to discuss and test Bitcoin strategies.</td>
  </tr>
  <tr>
    <td>09/25/2017</td>
    <td>Met with Prof. Brim to discuss pairs trading for Cryptocurrencies.</td>
  </tr>
  <tr>
    <td>10/02/2017</td>
    <td>Met with Prof. Brim to discuss correlation and cointegration for pairs trading.</td>
  </tr>
  <tr>
    <td>10/23/2017</td>
    <td>Met with Prof. Brim to discuss Vecm test for finding cointegration.</td>
  </tr>
  <tr>
    <td>11/06/2017</td>
    <td>Met with Prof. Brim to discuss different pairs trading strategies.</td>
  </tr>
  <tr>
    <td>12/04/2017</td>
    <td>Met with Prof. Brim to discuss mean reversion trading and optimal data handling.</td>
  </tr>
  <tr>
    <td>1/22/2018</td>
    <td>Met with Prof. Brim to discuss optimal moving average increments.</td>
  </tr>
</table>

## Research Sources
<ul>
<li><a href="https://quantopian.com">Quantopian</a></li>
<li><a href="https://www.quantconnect.com">QuantConnect</a></li>
<li><a href="http://investopedia.com">Investopedia</a></li>
<li><a href="https://robinhood.com">Robinhood Markets</a></li>
<li><a href="http://marketwatch.com">Market Watch</a></li>
<li><a href="http://stocktrading.com">Stock Trading</a></li>
</ul>

## Final Product
The final product will consist of a written report. Sample code and graphs for the performance of each algorithm will
be included in the report. All code will be displayed on this repository.
