#include <iostream>
#include <fstream>
#include <vector>


class Trader
{
    private:
        std::string ticker;//ticker symbol, i.e. aapl for Apple
        std::vector <float> prcs;//daily prices
        float profit;//total profit
        
    public:
        Trader(std::string);//prototype constructor
        void trade(bool);//trading simulation
        float getProfit();
};

//constructor
Trader::Trader(std::string t)
{
    ticker = t;
    profit = 0.0;
    
    //load stock prices for ticker
    std::string file = "prices/" + ticker + ".txt";
    std::ifstream fin;
    fin.open(file);
    float prc;
    if (fin.fail())
    {
        std::cout << "Cannot open file " + file + "\n";
    }
    else
    {
       while(!fin.eof())
        {
            fin >> prc;
            //std::cout << prc << "\n";
            prcs.push_back(prc);
        } 
    }
}

//trade function runs the trading simulation
void Trader::trade(bool output = false)
{
    float mavg5=0.0, buy=0.0, sell=0.0;
    int numTrades=0;
    for (int i=0;i<prcs.size();i++) {
        if(i>4)
        {
            mavg5=(prcs[i-1]+prcs[i-2]+prcs[i-3]+prcs[i-4]+prcs[i-5])/5.0;
            if(prcs[i]<(mavg5*0.97) and buy==0.0)//buy signal, price just went above 5 day avg
            {
                buy=prcs[i];
                if (output)
                {
                    std::cout << "--------" << std::endl << "day " << i << " bought at: " << buy << std::endl;
                }
            }
            else if (prcs[i]>(mavg5*1.03) and buy!=0.0) //sell signal, price just went below 5 day avg
            {
                numTrades++;
                sell=prcs[i];
                profit+=(sell-buy);
                if (output) 
                {
                    std::cout << "day " << i << " sold at: " << sell << std::endl << "trade profit: " << sell-buy << std::endl;
                }
                buy=0.0;
                sell=0.0;
            }
            else
            {
                //cout << "Do nothing, waiting for a buy signal or a sell signal" << endl;
            }
        }//if i
    }//for i
    
    if (output)
    {
        std::cout << std::endl << "----------------" << std::endl << "num trades for " << ticker << ": " << numTrades << std::endl << "----------------" << std::endl << std::endl;
    }

    
}//trade

//returns the profits of the Trader
float Trader::getProfit()
{
    std::cout << std::endl << "Initial investment for " << ticker << ": " << prcs[0] << ", we made: " << profit << std::endl;
    std::cout << "Percentage return for " << ticker << ": " << profit/prcs[0]*100.0 << "%" << std::endl;
    return profit;
}

int main()
{
    //creating many Traders, just add a ticker to tickers.txt and a csv to the prices folder
    std::vector <std::string> ticks;
    std::ifstream fin("tickers.txt");
    
    //loading stock tickers from tickers.txt
    std::string tmp;
    while (!fin.eof())
    {
        fin >> tmp; 
        ticks.push_back(tmp);
    }
    fin.close();
    
    //creating a vector of Traders
    std::vector <Trader*> myStocks;
    for (int i = 0; i < ticks.size(); i++)
    {
        myStocks.push_back(new Trader(ticks[i]));
    }

    //running trade(), trade simulation, for all myStocks
    for (int i = 0; i < myStocks.size(); i++)
    {
        myStocks[i]->trade(true);
    }
    
    //printing profits for all stocks traded
    for (int i = 0; i < myStocks.size(); i++)
    {
        myStocks[i]->getProfit();
    }
    
}