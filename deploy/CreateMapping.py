from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '192.168.52.2', 'port': 9200}])

REQUEST_MAPPING = {
    "mappings": {
        "v2": {
            "dynamic_templates": [
                {
                    "strings_as_keywords": {
                        "unmatch": "*_text",
                        "match_mapping_type": "string",
                        "mapping": {
                            "norms": "false",
                            "null_value": "NULL",
                            "type": "keyword"
                        }
                    }
                },
                {
                    "strings_as_texts": {
                        "match": "*_text",
                        "match_mapping_type": "string",
                        "mapping": {
                            "norms": "false",
                            "null_value": "NULL",
                            "type": "text"
                        }
                    }
                },
                {
                    "indexed_longs": {
                        "match_mapping_type": "long",
                        "mapping": {
                            "index": "true",
                            "type": "long"
                        }
                    }
                },
                {
                    "indexed_doubles": {
                        "match_mapping_type": "double",
                        "mapping": {
                            "index": "true",
                            "type": "float"
                        }
                    }
                }
            ],
            "properties": {
                "container_ip": {
                    "type": "string",
                    "index": "not_analyzed",
                    "null_value": "NULL"
                },
                "container_name": {
                    "type": "string",
                    "index": "not_analyzed",
                    "null_value": "NULL"
                },
                "timestamp": {
                    "type": "date"
                },
                "invoke_time": {
                    "type": "date"
                },
                "cal_time": {
                    "type": "date"
                },
                "network_tx_packets": {
                    "type": "long"
                },
                "network_rx_packets": {
                    "type": "long"
                },
                "pid_nums": {
                    "type": "long"
                },
                "memory_swap": {
                    "type": "long"
                },
                "memory_usage": {
                    "type": "long"
                },
                "memory_percent": {
                    "type": "double"
                },
                "cpu_percent": {
                    "type": "double"
                },
                "cpu_usage_in_kernelmod": {
                    "type": "long"
                },
                "cpu_usage_in_usermod": {
                    "type": "long"
                },
                "memory_limit": {
                    "type": "long"
                },
                "network_tx_bytes": {
                    "type": "long"
                },
                "network_rx_bytes": {
                    "type": "long"
                }
            }
        }
    }
}

status = es.indices.create(index="docker-final", ignore=400, body=REQUEST_MAPPING)

print status
