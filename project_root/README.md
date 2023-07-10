# Document Similarity Analyzer

This is a Django web application that allows users to upload one or multiple Word or PDF files, with a total size not exceeding 1GB per search. The application uses the transformers pretrained model `stsb-mpnet-base-v2` to ingest documents into a database after the upload is complete.

The purpose of this application is to quickly and effectively process multiple documents that have similarities. All content of all documents is represented on a categorized interactive list in order of degree of similarity. Duplicate content is listed once, with the number of times it appears and the name of the document(s) where it appears. 

Users can select any paragraph or sentence on the list to view it in its original context. The selected text will appear highlighted within the merged document bundle of the uploads. Users can delete or change list entries, and the uploaded document will be updated accordingly.

## Installation

1. Clone the repository: `git clone https://github.com/your-repo/document-similarity-analyzer.git`
2. Navigate to the project root: `cd document-similarity-analyzer`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the server: `python manage.py runserver`

## Usage

1. Open your web browser and navigate to `http://localhost:8000`.
2. Use the upload form to upload your Word or PDF files.
3. Wait for the documents to be processed and the similarities to be calculated.
4. View the results on the interactive list.
5. Select any paragraph or sentence to view it in its original context.
6. Delete or change list entries as needed.

## Note

If there are any issues with the code, please refer to the original algorithms at https://github.com/guenter-r/knn.git. Replace the code in `reuters` with the database of the ingested documents, unless it is to help refine our database, such as the stop words, etc. BeautifulSoup will not work for this application.