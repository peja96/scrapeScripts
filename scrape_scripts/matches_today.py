import time
import boto3
import os
import logging
from botocore.exceptions import ClientError

from selenium.webdriver.common.by import By
from scrape_scripts.init import get_driver


def upload_file_to_s3(source_dir, filename, bucket_name, bucket_object=None, client=None):
    if not client:
        client = boto3.client(
            's3',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
        )
    try:
        local_filepath = os.path.join(source_dir, filename)
        key = os.path.join(bucket_object, filename) if bucket_object else filename
        client.upload_file(local_filepath, bucket_name, key, ExtraArgs={'ContentType': 'text/plain'})
        logging.info('Uploaded file {} to bucket {} key {}'.format(
            local_filepath, bucket_name, key))
    except ClientError as e:
        logging.error(e)


def matches_today(url, filename):
    driver = get_driver()
    driver.get(url)
    time.sleep(1)
    rows = driver.find_elements(By.TAG_NAME, 'standard-item-info')
    matches = []
    for row in rows:
        home = row.find_element(By.CLASS_NAME, 'home').text
        away = row.find_element(By.CLASS_NAME, 'away').text
        game_time = row.find_element(By.CLASS_NAME, 'time').text
        matches.append(home + ',' + away + "|" + game_time)
        matches.append(away + ',' + home + "|" + game_time)

    new_path = os.path.join(os.getcwd(), '..', 'maps', filename)
    new_file = open(new_path, 'w')
    for match in matches:
        new_file.write(match + '\n')
    new_file.close()
    dir_path = os.path.join(os.getcwd(), '..', 'maps')
    upload_file_to_s3(dir_path, filename, 'playermaps')
    #driver.close()


if __name__ == "__main__":
    matches_today('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/sad/nba?leagueIds=77', 'nba_today.txt')
    matches_today('https://meridianbet.ba/sr/kladjenje/ko%C5%A1arka/evropa/euroleague?leagueIds=208', 'euroleague_today.txt')
