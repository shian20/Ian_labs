import csv
import requests
import logging
import json

logging.basicConfig(filename="log-file.txt",
                    level=logging.INFO,
                    format='[%(asctime)s]|%(levelname)s|\
                    %(module)s|%(lineno)d|%(message)s',)
log = logging.getLogger()


def ian_gateway(api_url, input_param):
    response = requests.post(api_url, data=json.dumps(input_param))
    # pdb.set_trace()
    print(response)


def process_valid_products(in_file):
    log_level = "WARNING"
    msg = "CSV file created"
    input_params = api_info(log_level, msg)
    log.warning(msg)
    ian_gateway(api_url, input_params)
    headers = None
    valid_products = []

    with open(in_file, newline='') as fh:
        reader = csv.DictReader(fh, fieldnames=headers)
        headers = reader.fieldnames
        for row in reader:
            if row.get('Categories'):
                valid_products.append(row)
    return headers, valid_products


def create_output_file(headers, valid_products):
    out_file = 'cleaned_products.csv'

    if headers and valid_products:
        with open(out_file, 'w', newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=headers)
            writer.writeheader()
            writer.writerows(valid_products)
    else:
        print('No valid products found!')
    log.critical(f"Output file written in: {out_file}")
    log_level = "CRITICAL"
    msg = "Successfully created a clean file"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)


def main(data_file):
    log_level = "ERROR"
    msg = "Identifying files"
    input_params = api_info(log_level, msg)
    log.error(msg)
    ian_gateway(api_url, input_params)
    headers, valid_products = process_valid_products(data_file)
    create_output_file(headers, valid_products)


def api_info(loglvl, note):
    parameters = {
        "email": "adrian.arcilla@globe.com.ph",
        "log_level": loglvl,
        "msg": note,
    }

    return parameters


if __name__ == '__main__':

    api_url = "https://dzkeujmt32.execute-api.us-east-1.amazonaws.com"\
              "/default/lambda_function_ian"

    data_file_in = 'https://raw.githubusercontent.com/woocommerce\
                /woocommerce/master/sample-data/sample_products.csv'

    log_level = "INFO"
    msg = "Initiating Process"
    input_params = api_info(log_level, msg)
    log.info(msg)
    ian_gateway(api_url, input_params)

    data_file_req = requests.get(data_file_in)
    url_content = data_file_req.content
    csv_file = open('raw_file.csv', 'wb').write(url_content)
    data_file = 'raw_file.csv'

    log_level = "DEBUG"
    msg = "Link instantiated"
    input_params = api_info(log_level, msg)
    log.debug(msg)
    ian_gateway(api_url, input_params)

    main(data_file)
