# Pairs Trading for Cryptocurrencies
Undergraduate Thesis for Michael Ward.  
Utah State University -- May 2018.
## Fundamental Goal
To learn algorithmic trading by creating and testing various algorithms with live market prices.

## Algorithms
### <a href="/Moving Averages/">Moving Averages</a>
Algorithms using the moving averages of the stock price over multiple days.

### <a href="/Mean Reversion/">Mean Reversion</a>
Improvement on Moving Averages where algorithms will place limits above and below the moving average.  
This will allow buy and sell times to more closely approach the highs and lows.

### Dynamic Mean Reversion
Improvement on Mean Reversion algorithm. Algorithm will dynamically change limits in accordance with stock's volatility.

### Pairs Trading
Finding the relationship between two or more prices.

## Results: Cryptocurrencies

### Moving Average Crossover on Bitcoin
With an initial investment of one Bitcoin and tested over a year, the algorithm returned:  
Total Profit:  $1,894.86  
Percent Return:  311.3%  
Percent Return (buying and holding):  659.1%  

\*\*While the algorithm returned less than buying and holding, moving average crossover may be more protected in case of a market crash. Further research will follow.

## Results: Stock Market

## Tasks
Pairs Trading:
- [ ] Dickey-Fuller algo in Python  
- [ ] Johansen cointegration test in Python (on Quantopian)  
- [ ] get past data
- [x] Create a Robinhood account and start trading by hand.
- [ ] Learn how the stock market works: optimal times to buy and sell and how to best predict future changes.
- [ ] Learn the basics of algorithmic trading.
- [ ] Learn Moving Averages Crossover strategy.
- [ ] Test Moving Averages Crossover strategy with Bitcoin.
- [ ] Modify MVA test with Bitcoin to find better results.
- [ ] Write my first algorithm.
- [ ] Refine my algorithm with past market data.
- [ ] Demo refined algorithm on Robinhood.
- [ ] Further refine algorithm using current market data.
- [ ] First Thesis Draft.
- [ ] Demo second iteration algorithm on Robinhood.
- [ ] Further refine second iteration of algorithm.
- [ ] Demo third iteration algorithm on Robinhood.
- [ ] Second Thesis Draft.
- [ ] Further refine third iteration for report.
- [ ] Choose key algorithms and discover important ideas.
- [ ] Penultimate Thesis Draft
- [ ] Final Thesis Submission
- [ ] Present Thesis at Research Symposium

## Timeline

<table>
  <tr>
    <td>05/31/2017</td>
    <td>Created an account on Robinhood and started trading by hand.</td>
  </tr>
  <tr>
    <td>09/01/2017</td>
    <td>Demo my first algorithm on Robinhood. Results will be taken for the next 8 months.</td>
  </tr>
  <tr>
    <td>12/20/2017</td>
    <td>Demo next iteration of algorithms on Robinhood. Results will be taken for the next 4 months.</td>
  </tr>
  <tr>
    <td>03/01/2018</td>
    <td>Demo final iteration of algorithms on Robinhood. Results will be taken for the next 2 months.</td>
  </tr>
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
</table>

## Research Sources
<ul>
<li><a href="https://quantopian.com">Quantopian</a></li>
<li><a href="http://investopedia.com">Investopedia</a></li>
<li><a href="https://robinhood.com">Robinhood Markets</a></li>
<li><a href="http://marketwatch.com">Market Watch</a></li>
<li><a href="http://stocktrading.com">Stock Trading</a></li>
</ul>

## Final Product
The final product will consist of a written report. Sample code and graphs for the performance of each algorithm will
be included in the report. All code will be displayed on this repository.
