# news-aggregator
Small app that scrapes the news articles from four romanian news sites and displays them on a single web page.

- Four python scripts which scrape each website. They are all wrapped in a bash script in which I export the environment variables necessary for the execution; 
- A cron job executes the bash script every two minutes. The scrapers add the new links in the database - if the same link exists, it gets skipped;
- All results are displayed on a four column grid, one for every website;
- The users have the option to search for every link stored in the database and the results are displayed in a descending order;
