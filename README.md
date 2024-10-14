# Weekly Report Automation

## Data Collection
From the list of social media handles provided every iteration, we first automate the creation of RivalIQ trial accounts with tempmail accounts. We use a combination of undetected chrome drivers and tor drivers for this purpose. We then download the file from each account.
temp_mail_creation_download.ipynb serves this purpose.

## Data Processing
We calculate all the becessary metrics and map them with corresponding entities from the mapping file. We export 4 different files at the end of this process. 
We run data_processing.ipynb to generate:
1) A raw data excel file with 4 sheets(one for each platform) to push into the database
2) A processed excel with 8 sheets; 2 per platform one for pre and post duration metrics
3) A processed excel wiht 4 sheets; 1 sheet per platform for overall duration metrics
4) A processed excel with 4 sheets; 1 per platform for 7 day moving average

## Bar Chart Generation 
From the pre and post duration metrics computed earlier, we plot absolute value and change % bar plots for all the generated metrics and store it in a folder folder structure
bar_chart_generation_final.ipynb serves this purpose.

## PPT Generation
We automate the generation of the PPT that is attached using all the excel files and bar charts that have been generated so far
