import pandas as pd

class NJCleaner():
    def __init__(self, csv_path: str)->None:
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self) ->pd.DataFrame:
        order = self.data.sort_values(by=['scheduled_time'])
        return order
    
    def drop_columns_and_nan(self):
        df = self.data.drop(columns=['from'])
        df = self.data.drop(columns=['to'])        
        df = df.dropna()
        return df

    def convert_date_to_day(self):
        df = self.data
        df['day'] = pd.to_datetime(df['date']).dt.day_name()
        df = df.drop(columns=['date'])
        return df
    
    def convert_scheduled_time_to_part_of_the_day(self)->pd.DataFrame:
        df = self.data
        df['scheduled_time'] = pd.to_datetime(df['scheduled_time'])
        xc = df['scheduled_time'].dt.hour
        df['part_of_the_day'] = xc.apply(lambda x: 
                                        'early morning' if 4 <= x < 8 else
                                        'morning' if 8 <= x < 12 else
                                        'afternoon' if 12<= x <16 else
                                        'evening' if 16<= x < 20 else
                                        'late_night' if x < 4 else
                                        'night')
        df = self.data.drop(columns=['scheduled_time'])    
        return df 






    def pred_df(self):
        pass


    