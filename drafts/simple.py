from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("collect").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    inputWords = ["spark", "hadoop", "spark", "hive", "pig", "cassandra", "hadoop"]

    wordRdd = sc.parallelize(inputWords, 2)
    wordRdd.foreach(lambda x: print(x))
