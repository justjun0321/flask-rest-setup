# Machine Learning Model as a REST API using Flask (Merpay)

* [Flask Restful Documentation](https://flask-restful.readthedocs.io/en/latest/)
* [HTTPie](https://httpie.org/doc)
___

## Steos
1. Create a virtual environment and install requirements
3. Build Model and save to pickle file
4. Add `app.py` as the API application
5. Create requirements.txt for current requirements
6. Test the API using terminal


## File Structure
* lib
  * data
    * test.csv: data for testing
    * train.csv: data for model building
  * model
    * model.pkl: supervised prediction model built using Logistic Regression
* Modeling.ipynb: jupyter notebook for model building and testing of model loading
* app.py: Flask Restful API application
* requirements.txt: requirements for application deployment

## Testing the API
1. Run the Flask Restful API on local side for testing. Go to directory where `app.py` is saved.

```bash
python app.py
```


2. Open a new terminal, use HTTPie to send a GET request to the API.

```bash
http http://127.0.0.1:5000/ -d data_path='lib/data/test.csv'
```


3. Example of successful output.

```bash
{
    item_id: prediction
}
```

4. Deploying the Flask app on an EC2 instance or on Google App Engine.
