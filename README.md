# ASIRS
This is my final project for Morden Information Retrieve course in XMU. I implement ASIRS (A Simple Information Retrieval System) by Python 3.6. The algorithm is proposed in the paper [Probabilistic Query Expansion Using Query Logs], you can read it for details.

## Documents Set
You can find all documents in `datafile` directory. I provide 20 short passages from CNN. The first line of document is the title. The following paragraphs are divided by blank line. Each line has only one paragraph.

## Log File
For the sake of simplicity, we use `txt` file to store the log infomation. All the logs are stored in `log.txt`. Each line represents a query record. The first word is keyword, followed by a space. The list of numbers divided by comma mark is the No. of clicked documents when user search that keyword.

For example, you search **food**, and the system returns several documents. You click No. 8, 9, 11 and 12. It represents that these documents are relevant to your demand. So when you search "food" next time, the system will give priority to them.

## How to Use?
The entry is in `query.py`. You can change `dir_path` and `doc_number` to the right path of documents and the number of documents at the end of file. 

Then you can enter the keywords divided by space that you want to search. The system will return several documents with the No., title and abstract. The keyword in abstract will be surrounded by star mark (*). You need enter the No. of docs satisfy your need, question mark (?) stands for none. 

You can enter `q` to quit the system.

## Reference
[1] Cui, Hang, et al. "Probabilistic query expansion using query logs." International Conference on World Wide Web ACM, 2002:325-332.

[Probabilistic Query Expansion Using Query Logs]: http://vela.cs.ust.hk/readinglist/p325-cui.pdf