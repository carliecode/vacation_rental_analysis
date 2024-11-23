import pandas as pd
import utils

def task_one():
    try:
        columns = ['host_is_superhost', 'neighbourhood_cleansed', 'price']
        data = utils.load_file(utils.LISTING_FILE, columns, True)

        super_host = data[data['host_is_superhost'] == 't']
        non_super_host = data[data['host_is_superhost'] == 'f']
        super_host = super_host.groupby('neighbourhood_cleansed')['price'].median()
        non_super_host = non_super_host.groupby('neighbourhood_cleansed')['price'].median()
        data = pd.DataFrame({
                'median_super_host': super_host,
                'median_non_super_host': non_super_host
                })

        data['median_differennce'] = data['median_super_host'] - data['median_non_super_host']
        neighbourhood = data['median_differennce'].idxmax()
        median =  data[data.index == neighbourhood]['median_differennce'][0]
        
        print(f'The neighbourhood with the higest median comparison between superhost and non superhost is:  {neighbourhood}')
        print(f'The median value is: {median}')

    except Exception as e:
        raise

    
def task_two():
    try:
        columns = [
                'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 
                'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 
                'review_scores_value']
        data = utils.load_file(utils.LISTING_FILE, columns, True)
        correlation = data[[
                'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 
                'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 
                'review_scores_value']].corrwith(data['price'])
        highest_correlation_review = correlation.abs().idxmax()
        correlation_value = correlation[highest_correlation_review]        

        print(f'The review variable with the highest correlation with [price] is: {highest_correlation_review}')
        print(f'The value is: {float(correlation_value).__round__(2)}')
    except:
        raise


def task_three():
    try:
        columns = ['host_id', 'neighbourhood_cleansed', 'price']
        data = utils.load_file(utils.LISTING_FILE, columns, True)

        host_locations =  data.groupby('host_id')['neighbourhood_cleansed'].nunique()
        prof_host_ids = host_locations[host_locations > 5].index
        prof_host_data = data[data['host_id'].isin(prof_host_ids)]
        nprof_host_data = data[~data['host_id'].isin(prof_host_ids)]

        prof_mean = prof_host_data['price'].mean()
        nprof_mean = nprof_host_data['price'].mean()

       
        print(prof_mean - nprof_mean)   

    except:
        raise



def task_four():
    try:
        columns = ['room_type', 'neighbourhood_cleansed', 'price']
        data = utils.load_file(utils.LISTING_FILE, columns, True)
        
        entire_home_listing = data[data['room_type'] == 'Entire home/apt']
        other_listings = data[data['room_type'] != 'Entire home/apt']

        median_entire_home = entire_home_listing.groupby('neighbourhood_cleansed')['price'].mean()
        other_listings = other_listings.groupby('neighbourhood_cleansed')['price'].mean()

        premium_price =  median_entire_home - other_listings
        print(premium_price)
    except:
        raise


if __name__ == '__main__':
    try:
        task_four()
    except:
        raise