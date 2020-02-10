---
title: "Knapsack Algorithm"
date: 2019-06-01
tags: [Projects]
---

##### Tokenize text and Convert to word2vec using Spark

```python
#create a spark and SQL context
sc = SparkSession.builder.appName(APP_NAME).master(SPARK_URL).getOrCreate()
sqlContext = SQLContext(sc)

#load data
amzn_data = sqlContext.read.json(DATA_NAME)	

#check the shape
print(f'Dataset shape is {amzn_data.count():d} rows by {len(amzn_data.columns):d} columns.')
```

Dataset shape is 134476 rows by 9 columns.

```python
#register a temp table
amzn_data.registerTempTable('reviews')

#write sql query to see each count by each review
sqlContext.sql("select overall, count(overall) as reviewCount from reviews group by overall order by overall desc").show()
```
+-------+-----------+
|overall|reviewCount|
+-------+-----------+
|    5.0|      85266|
|    4.0|      28336|
|    3.0|      10769|
|    2.0|       4962|
|    1.0|       5143|
+-------+-----------+

```python
#combine reviews >3 and <=3
udf = UserDefinedFunction(lambda x: 1 if x > 3.0 else -1, IntegerType())
amzn_data_ = amzn_data.withColumn("overall_recode",udf(amzn_data.overall))

amzn_data_.select("overall", "overall_recode", "summary", "reviewText").show(10)
```
+-------+--------------+--------------------+--------------------+
|overall|overall_recode|             summary|          reviewText|
+-------+--------------+--------------------+--------------------+
|    5.0|             1|Perfect for colla...|I hate it when my...|
|    5.0|             1|                Neat|These little magn...|
|    5.0|             1| Very small and thin|I wanted somethin...|
|    5.0|             1|Excellent hobby m...|I use these to ma...|
|    5.0|             1|They're annoying....|They are soo frea...|
|    5.0|             1|       using for 40k|am using for 40k ...|
|    5.0|             1|Great source book...|The color picture...|
|    3.0|            -1|Good for starting...|Good simple proje...|
|    5.0|             1|      Fantastic book|These are project...|
|    5.0|             1|  AWESOME!!!!!!!!!!!|If you have a poc...|
+-------+--------------+--------------------+--------------------+
only showing top 10 rows

```python
#turn text data into tokens
tokenizer = Tokenizer(inputCol="reviewText", outputCol="tokenized_text").transform(amzn_data_)

#convert tokenized data to word2vec vector
word2Vec = Word2Vec(vectorSize=300, seed=42, inputCol="tokenized_text", outputCol="w2v_vector").fit(tokenizer)

w2vdf=word2Vec.transform(tokenizer)

#show output
w2vdf.select("overall_recode","reviewText","tokenized_text","w2v_vector").show(10)
```

+--------------+--------------------+--------------------+--------------------+
|overall_recode|          reviewText|      tokenized_text|          w2v_vector|
+--------------+--------------------+--------------------+--------------------+
|             1|I hate it when my...|[i, hate, it, whe...|[0.04722892069889...|
|             1|These little magn...|[these, little, m...|[0.05201734777475...|
|             1|I wanted somethin...|[i, wanted, somet...|[0.03429755460181...|
|             1|I use these to ma...|[i, use, these, t...|[0.03781380703938...|
|             1|They are soo frea...|[they, are, soo, ...|[0.02663341721571...|
|             1|am using for 40k ...|[am, using, for, ...|[0.04175524418263...|
|             1|The color picture...|[the, color, pict...|[0.05472110957634...|
|            -1|Good simple proje...|[good, simple, pr...|[0.08049255864823...|
|             1|These are project...|[these, are, proj...|[0.04887839956095...|
|             1|If you have a poc...|[if, you, have, a...|[0.06934023722104...|
+--------------+--------------------+--------------------+--------------------+
only showing top 10 rows