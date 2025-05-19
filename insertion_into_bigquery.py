import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText, WriteToText,  ReadFromCsv, WriteToBigQuery
import logging
from collections import defaultdict
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "<SA secret file path>"

# class CsvToJsonFn(beam.DoFn):
#
#     def process(self, element):
#         labels = ['job_posted_date', 'company_address_locality', 'company_address_region', 'company_name', 'company_website', 'company_description', 'job_description_text', 'seniority_level', 'job_title']
#         print(element.split(","))
#         return 1

def process(element):
    labels = ('job_posted_date', 'company_address_locality', 'company_address_region', 'company_name',
              'company_website', 'company_description', 'job_description_text', 'seniority_level', 'job_title')
    # print(element)
    # values = element.split(",")
    # return dict(zip(labels, values))

    values = json.loads(json.dumps(element))
    # print(values)
    return dict(zip(labels, values))

def run(parser_obj):
    """
    :param parser_obj:

    the text between '|'  and '>>' defines the name of the step, used for display purposes
    """
    known_args, pipeline_args = parser_obj.parse_known_args()
    pipeline_options = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_options) as p:

        stages = (
                p
                | "READ" >> ReadFromCsv(known_args.input, splittable=False, index_col=0)
                | "TRANSFORM" >> beam.Map(process)
        )

        output_pc = stages | "WRITE" >> WriteToBigQuery(known_args.output,  # --output
                                                        schema="job_posted_date:DATE, company_address_locality:STRING, "
                                                               "company_address_region:STRING, company_name:STRING, "
                                                               "company_website:STRING, company_description:STRING,"
                                                               "job_description_text:STRING, seniority_level:STRING, job_title:STRING",
                                                        )


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        help="the input file path, format-> gs://<bucket>/<file_path>",
                        required=True)

    parser.add_argument("--output",
                        help="the output file path, format-> <project>:<dataset>.<table_name>",
                        required=True)

    run(parser)

