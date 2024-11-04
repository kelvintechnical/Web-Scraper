# Books Scraper Repository

## Overview
The Books Scraper repository is a web scraping project aimed at extracting book titles and prices from the [Books to Scrape](https://books.toscrape.com/) website. The project leverages Python's `requests` library to fetch HTML content and `BeautifulSoup` for parsing and navigating the HTML structure. The extracted data is then saved into a CSV file for further analysis.

## Lessons Learned
While building this project, I gained valuable experience and insights, particularly in the following areas:
1. **Web Scraping Techniques**: Mastered the use of `requests` to send HTTP GET requests and fetch webpage content. Utilized `BeautifulSoup` for parsing HTML, extracting specific data points like book titles and prices, and understanding the importance of checking HTTP response status codes for successful data retrieval.
2. **Data Handling and Storage**: Developed skills in handling and storing data by creating and managing CSV files using Python's `csv` module. Learned to structure data in a meaningful way for analysis and sharing.
3. **Error Handling and Debugging**: Enhanced my ability to troubleshoot and debug issues by implementing error handling mechanisms. Understood the significance of response status codes in diagnosing potential problems with web requests.

## Graph
Here is an embedded graph illustrating the book prices analysis:
<div class='tableauPlaceholder' id='viz1730764519605' style='position: relative'><noscript><a href='#'><img alt='Sheet 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;BookPriceAnalysis&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='BookPriceAnalysis&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;BookPriceAnalysis&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1730764519605');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width='100%';
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
Or you can view the graph directly [here](https://public.tableau.com/views/BookPriceAnalysis/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

## Follow Me
If you find this project interesting and want to stay updated with my latest work, follow me on Twitter: [Follow me on Twitter](https://x.com/kelvinintech)
