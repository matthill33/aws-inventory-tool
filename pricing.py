# There is no good tool out there for retrieving real time on-demand prices
# The prices for this tool will be hard coded using dictionaries
# On-demand prices are subject to change, but the changes will most likely be negligible

# dict of us-east-1 ec2 on demand prices as of 8/6/21
ec2_pricing_dict = {
'a1.medium' : 0.0255,
'a1.large' : 0.051,
'a1.xlarge' : 0.102,
'a1.2xlarge' : 0.204,
'a1.4xlarge' : 0.408,
'a1.metal' : 0.408,

't4g.nano' : 0.0042,
't4g.micro' : 0.0084,
't4g.small' : 0.0168,
't4g.medium' : 0.0336,
't4g.large' : 0.0672,
't4g.xlarge' : 0.1344,
't4g.2xlarge' : 0.2688,

't2.nano': 0.0058,
't2.micro': 0.0116,
't2.small': 0.023,
't2.medium': 0.0464,
't2.large': 0.0928,
't2.xlarge': 0.1856,
't2.2xlarge': 0.3712,

't3.nano': 0.0052,
't3.micro': 0.0104,
't3.small': 0.0208,
't3.medium': 0.0416,
't3.large': 0.0832,
't3.xlarge': 0.1664,
't3.2xlarge': 0.3328,
't3a.nano': 0.0047,
't3a.micro': 0.0094,
't3a.small': 0.0188,
't3a.medium': 0.0376,
't3a.large': 0.0752,
't3a.xlarge': 0.1504,
't3a.2xlarge': 0.3008,

'm5.large': 0.096,
'm5.xlarge': 0.192,
'm5.2xlarge': 0.384,
'm5.4xlarge': 0.768,
'm5.8xlarge': 1.536,
'm5.12xlarge': 2.304,
'm5.16xlarge': 3.072,
'm5.24xlarge': 4.608,
'm5.metal': 4.608,

'm5a.large': 0.086,
'm5a.xlarge': 0.172,
'm5a.2xlarge': 0.344,
'm5a.4xlarge': 0.688,
'm5a.8xlarge': 1.376,
'm5a.12xlarge': 2.064,
'm5a.16xlarge': 2.752,
'm5a.24xlarge': 4.128,
'm5ad.large': 0.103,
'm5ad.xlarge': 0.206,
'm5ad.2xlarge': 0.412,
'm5ad.4xlarge': 0.824,
'm5ad.8xlarge': 1.648,
'm5ad.12xlarge': 2.472,
'm5ad.16xlarge': 3.296,
'm5ad.24xlarge': 4.944,

'm5d.large': 0.113,
'm5d.xlarge': 0.226,
'm5d.2xlarge': 0.452,
'm5d.4xlarge': 0.904,
'm5d.8xlarge': 1.808,
'm5d.12xlarge': 2.712,
'm5d.16xlarge': 3.616,
'm5d.24xlarge': 5.424,
'm5d.metal' : 5.424,

'm5dn.large' : 0.136,
'm5dn.xlarge' : 0.272,
'm5dn.2xlarge' : 0.544,
'm5dn.4xlarge' : 1.088,
'm5dn.8xlarge' : 2.176,
'm5dn.12xlarge' : 3.264,
'm5dn.16xlarge' : 4.352,
'm5dn.24xlarge' : 6.528,
'm5dn.metal' : 6.528,

'm5n.large' : 0.119,
'm5n.xlarge' : 0.238,
'm5n.2xlarge' : 0.476,
'm5n.4xlarge' : 0.952,
'm5n.8xlarge' : 1.904,
'm5n.12xlarge' : 2.856,
'm5n.16xlarge' : 3.808,
'm5n.24xlarge' : 5.712,
'm5n.metal' : 5.712,

'm5zn.large' : 0.1652,
'm5zn.xlarge' : 0.3303,
'm5zn.2xlarge' : 0.6607,
'm5zn.3xlarge' : 0.991,
'm5zn.6xlarge' : 1.982,
'm5zn.12xlarge' : 3.9641,
'm5zn.metal' : 3.9641,

'm6g.medium' : 0.0385,
'm6g.large' : 0.077,
'm6g.xlarge' : 0.154,
'm6g.2xlarge' : 0.308,
'm6g.4xlarge' : 0.616,
'm6g.8xlarge' : 1.232,
'm6g.12xlarge' : 1.848,
'm6g.16xlarge' : 2.464,
'm6g.metal' : 2.464,
'm6gd.medium' : 0.0452,
'm6gd.large' : 0.0904,
'm6gd.xlarge' : 0.1808,
'm6gd.2xlarge' : 0.3616,
'm6gd.4xlarge' : 0.7232,
'm6gd.8xlarge' : 1.4464,
'm6gd.12xlarge' : 2.1696,
'm6gd.16xlarge' : 2.8928,
'm6gd.metal' : 2.8928,

'c4.large' : 0.10,
'c4.xlarge' : 0.199,
'c4.2xlarge' : 0.398,
'c4.4xlarge' : 0.796,
'c4.8xlarge' : 1.591,

'c5.large' : 0.085,
'c5.xlarge' : 0.17,
'c5.2xlarge' : 0.34,
'c5.4xlarge' : 0.68,
'c5.9xlarge' : 1.53,
'c5.12xlarge' : 2.04,
'c5.24xlarge' : 3.06,

'c5a.large' : 0.077,
'c5a.xlarge' : 0.154,
'c5a.2xlarge' : 0.308,
'c5a.4xlarge' : 0.616,
'c5a.8xlarge' : 1.232,
'c5a.12xlarge' : 1.848,
'c5a.16xlarge' : 2.464,
'c5a.24xlarge' : 3.696,

'c5d.large' : 0.096,
'c5d.xlarge' : 0.192,
'c5d.2xlarge' : 0.384,
'c5d.4xlarge' : 0.768,
'c5d.9xlarge' : 1.728,
'c5d.12xlarge' : 2.304,
'c5d.18xlarge' : 3.456,
'c5d.24xlarge' : 4.608,
'c5d.metal' : 4.608,

'c5n.large' : 0.108,
'c5n.xlarge' : 0.216,
'c5n.2xlarge' : 0.432,
'c5n.4xlarge' : 0.864,
'c5n.9xlarge' : 1.944,
'c5n.18xlarge' : 3.888,
'c5n.metal' : 3.888,

'c5ad.large' : 0.086,
'c5ad.xlarge' : 0.172,
'c5ad.2xlarge' : 0.344,
'c5ad.4xlarge' : 0.688,
'c5ad.8xlarge' : 1.376,
'c5ad.12xlarge' : 2.064,
'c5ad.16xlarge' : 2.752,
'c5ad.24xlarge' : 4.128,

'c6g.medium' : 0.034,
'c6g.large' : 0.068,
'c6g.xlarge' : 0.136,
'c6g.2xlarge' : 0.272,
'c6g.4xlarge' : 0.544,
'c6g.8xlarge' : 1.088,
'c6g.12xlarge' : 1.632,
'c6g.16xlarge' : 2.176,
'c6g.metal' : 2.176,

'c6gd.medium' : 0.0384,
'c6gd.large' : 0.0768,
'c6gd.xlarge' : 0.1536,
'c6gd.2xlarge' : 0.3072,
'c6gd.4xlarge' : 0.6144,
'c6gd.8xlarge' : 1.2288,
'c6gd.12xlarge' : 1.8432,
'c6gd.16xlarge' : 2.4576,
'c6gd.metal' : 2.4576,

'c6gn.medium' : 0.0432,
'c6gn.large' : 0.0864,
'c6gn.xlarge' : 0.1728,
'c6gn.2xlarge' : 0.3456,
'c6gn.4xlarge' : 0.6912,
'c6gn.8xlarge' : 1.3824,
'c6gn.12xlarge' : 2.0736,
'c6gn.16xlarge' : 2.7648,

'r5.large' : 0.126,
'r5.xlarge' : 0.252,
'r5.2xlarge' : 0.504,
'r5.4xlarge' : 1.008,
'r5.8xlarge' : 2.016,
'r5.12xlarge' : 3.024,
'r5.16xlarge' : 4.032,
'r5.24xlarge' : 6.048,
'r5.metal' : 6.048,

'r5a.large' : 0.113,
'r5a.xlarge' : 0.226,
'r5a.2xlarge' : 0.452,
'r5a.4xlarge' : 0.904,
'r5a.8xlarge' : 1.808,
'r5a.12xlarge' : 2.712,
'r5a.16xlarge' : 3.616,
'r5a.24xlarge' : 5.424,

'r5b.large' : 0.149,
'r5b.xlarge' : 0.298,
'r5b.2xlarge' : 0.596,
'r5b.4xlarge' : 1.192,
'r5b.8xlarge' : 2.384,
'r5b.12xlarge' : 3.576,
'r5b.16xlarge' : 4.768,
'r5b.24xlarge' : 7.152,
'r5b.metal' : 7.152,

'r5d.large' : 0.144,
'r5d.xlarge' : 0.288,
'r5d.2xlarge' : 0.576,
'r5d.4xlarge' : 1.152,
'r5d.8xlarge' : 2.304,
'r5d.12xlarge' : 3.456,
'r5d.16xlarge' : 4.608,
'r5d.24xlarge' : 6.912,
'r5d.metal' : 6.912,

'r5n.large' : 0.149,
'r5n.xlarge' : 0.298,
'r5n.2xlarge' : 0.596,
'r5n.4xlarge' : 1.192,
'r5n.8xlarge' : 2.384,
'r5n.12xlarge' : 3.576,
'r5n.16xlarge' : 4.768,
'r5n.24xlarge' : 7.152,
'r5n.metal' : 7.152,

'r5dn.large' : 0.167,
'r5dn.xlarge' : 0.334,
'r5dn.2xlarge' : 0.668,
'r5dn.4xlarge' : 1.336,
'r5dn.8xlarge' : 2.672,
'r5dn.12xlarge' : 4.008,
'r5dn.16xlarge' : 5.344,
'r5dn.24xlarge' : 8.016,
'r5dn.metal' : 8.016,

'r5ad.large' : 0.131,
'r5ad.xlarge' : 0.262,
'r5ad.2xlarge' : 0.524,
'r5ad.4xlarge' : 1.048,
'r5ad.8xlarge' : 2.096,
'r5ad.12xlarge' : 3.144,
'r5ad.16xlarge' : 4.192,
'r5ad.24xlarge' : 6.288,

'r6g.medium' : 0.0504,
'r6g.large' : 0.1008,
'r6g.xlarge' : 0.2016,
'r6g.2xlarge' : 0.4032,
'r6g.4xlarge' : 0.8064,
'r6g.8xlarge' : 1.6128,
'r6g.12xlarge' : 2.4192,
'r6g.16xlarge' : 3.2256,
'r6g.metal' : 3.2256,

'r6gd.medium' : 0.0576,
'r6gd.large' : 0.1152,
'r6gd.xlarge' : 0.2304,
'r6gd.2xlarge' : 0.4608,
'r6gd.4xlarge' : 0.9216,
'r6gd.8xlarge' : 1.8432,
'r6gd.12xlarge' : 2.7648,
'r6gd.16xlarge' : 3.6864,
'r6gd.metal' : 3.6864,

'r4.large' : 0.133,
'r4.xlarge' : 0.266,
'r4.2xlarge' : 0.532,
'r4.4xlarge' : 1.064,
'r4.8xlarge' : 2.128,
'r4.16xlarge' : 4.256,

'p2.xlarge' : 0.90,
'p2.8xlarge' : 7.20,
'p2.16xlarge' : 14.4,

'p3.2xlarge' : 3.06,
'p3.8xlarge' : 12.24,
'p3.16xlarge' : 24.48,
'p4d.24xlarge' : 32.7726,

'g4ad.xlarge' : 0.37853,
'g4ad.2xlarge' : 0.54117,
'g4ad.4xlarge' : 0.867,
'g4ad.8xlarge' : 1.734,
'g4ad.16xlarge' : 3.468,

'g4dn.xlarge' : 0.526,
'g4dn.2xlarge' : 0.752,
'g4dn.4xlarge' : 1.204,
'g4dn.8xlarge' : 2.176,
'g4dn.12xlarge' : 3.912,
'g4dn.16xlarge' : 4.352,
'g4dn.metal' : 7.824,

'g3.4xlarge' : 1.14,
'g3.8xlarge' : 2.28,
'g3.16xlarge' : 4.56,
'g3s.xlarge' : 0.75,

'x2gd.medium' : 0.0835,
'x2gd.large' : 0.167,
'x2gd.xlarge' : 0.334,
'x2gd.2xlarge' : 0.668,
'x2gd.4xlarge' : 1.336,
'x2gd.8xlarge' : 2.672,
'x2gd.12xlarge' : 4.008,
'x2gd.16xlarge' : 5.344,
'x2gd.metal' : 5.344,
}

# dict of us-east-1 rds aurora on demand prices as of 8/6/21
# mysql and postgresql prices were exactly the same as of 8/6/21
rds_aurora_pricing_dict = {
'db.t3.small' : 0.041,
'db.t3.medium' : 0.082,
'db.t3.large' : 0.164,

'db.r6g.large' : 0.26,
'db.r6g.xlarge' : 0.519,
'db.r6g.2xlarge' : 1.038,
'db.r6g.4xlarge' : 2.076,
'db.r6g.8xlarge' : 4.153,
'db.r6g.12xlarge' : 6.229,
'db.r6g.16xlarge' : 8.306,

'db.r5.large' : 0.29,
'db.r5.xlarge' : 0.58,
'db.r5.2xlarge' : 1.16,
'db.r5.4xlarge' : 2.32,
'db.r5.8xlarge' : 4.64,
'db.r5.12xlarge' : 6.96,
'db.r5.16xlarge' : 9.28,
'db.r5.24xlarge' : 13.92,

'db.t2.small' : 0.041,
'db.t2.medium' : 0.082,

'db.r4.large' : 0.29,
'db.r4.xlarge' : 0.58,
'db.r4.2xlarge' : 1.16,
'db.r4.4xlarge' : 2.32,
'db.r4.8xlarge' : 4.64,
'db.r4.16xlarge' : 9.28,

'db.r3.large' : 0.29,
'db.r3.xlarge' : 0.58,
'db.r3.2xlarge' : 1.16,
'db.r3.4xlarge' : 2.32,
'db.r3.8xlarge' : 4.64
}

# dict of us-east-1 rds mysql on demand prices as of 8/6/21
rds_mysql_pricing_dict = {
'db.t3.micro' : 0.017,
'db.t3.small' : 0.034,
'db.t3.medium' : 0.068,
'db.t3.large' : 0.136,
'db.t3.xlarge' : 0.272,
'db.t3.2xlarge' : 0.544,

'db.m6g.large' : 0.152,
'db.m6g.xlarge' : 0.304,
'db.m6g.2xlarge' : 0.608,
'db.m6g.4xlarge' : 1.216,
'db.m6g.8xlarge' : 2.432,
'db.m6g.12xlarge' : 3.648,
'db.m6g.16xlarge' : 4.864,

'db.m5.large' : 0.171,
'db.m5.xlarge' : 0.342,
'db.m5.2xlarge' : 0.684,
'db.m5.4xlarge' : 1.368,
'db.m5.8xlarge' : 2.74,
'db.m5.12xlarge' : 4.104,
'db.m5.16xlarge' : 5.47,
'db.m5.24xlarge' : 8.208,

'db.r6g.large' : 0.215,
'db.r6g.xlarge' : 0.43,
'db.r6g.2xlarge' : 0.859,
'db.r6g.4xlarge' : 1.718,
'db.r6g.8xlarge' : 3.437,
'db.r6g.12xlarge' : 5.155,
'db.r6g.16xlarge' : 6.874,

'db.r5.large' : 0.24,
'db.r5.xlarge' : 0.48,
'db.r5.2xlarge' : 0.96,
'db.r5.4xlarge' : 1.92,
'db.r5.8xlarge' : 3.84,
'db.r5.12xlarge' : 5.76,
'db.r5.16xlarge' : 7.68,
'db.r5.24xlarge' : 11.52,

'db.t2.micro' : 0.017,
'db.t2.small' : 0.034,
'db.t2.medium' : 0.068,
'db.t2.large' : 0.136,
'db.t2.xlarge' : 0.272,
'db.t2.2xlarge' : 0.544,

'db.m4.large' : 0.175,
'db.m4.xlarge' : 0.35,
'db.m4.2xlarge' : 0.70,
'db.m4.4xlarge' : 1.401,
'db.m4.10xlarge' : 3.502,
'db.m4.16xlarge' : 5.60,

'db.r4.large' : 0.24,
'db.r4.xlarge' : 0.48,
'db.r4.2xlarge' : 0.96,
'db.r4.4xlarge' : 1.92,
'db.r4.8xlarge' : 3.84,
'db.r4.16xlarge' : 7.68,

'db.r3.large' : 0.24,
'db.r3.xlarge' : 0.475,
'db.r3.2xlarge' : 0.945,
'db.r3.4xlarge' : 1.89,
'db.r3.8xlarge' : 3.78
}

# dict of us-east-1 rds postgresql on demand prices as of 8/6/21
rds_postgres_pricing_dict = {
'db.t3.micro' : 0.018,
'db.t3.small' : 0.036,
'db.t3.medium' : 0.072,
'db.t3.large' : 0.145,
'db.t3.xlarge' : 0.29,
'db.t3.2xlarge' : 0.579,

'db.m6g.large' : 0.159,
'db.m6g.xlarge' : 0.318,
'db.m6g.2xlarge' : 0.636,
'db.m6g.4xlarge' : 1.272,
'db.m6g.8xlarge' : 2.544,
'db.m6g.12xlarge' : 3.816,
'db.m6g.16xlarge' : 5.088,

'db.m5.large' : 0.178,
'db.m5.xlarge' : 0.356,
'db.m5.2xlarge' : 0.712,
'db.m5.4xlarge' : 1.424,
'db.m5.8xlarge' : 2.848,
'db.m5.12xlarge' : 4.272,
'db.m5.16xlarge' : 5.696,
'db.m5.24xlarge' : 8.544,

'db.r6g.large' : 0.225,
'db.r6g.xlarge' : 0.45,
'db.r6g.2xlarge' : 0.899,
'db.r6g.4xlarge' : 1.798,
'db.r6g.8xlarge' : 3.597,
'db.r6g.12xlarge' : 5.395,
'db.r6g.16xlarge' : 7.194,

'db.r5.large' : 0.25,
'db.r5.xlarge' : 0.50,
'db.r5.2xlarge' : 1.00,
'db.r5.4xlarge' : 2.00,
'db.r5.8xlarge' : 4.00,
'db.r5.12xlarge' : 6.00,
'db.r5.16xlarge' : 8.00,
'db.r5.24xlarge' : 12.00,

'db.t2.micro' : 0.018,
'db.t2.small' : 0.036,
'db.t2.medium' : 0.073,
'db.t2.large' : 0.145,
'db.t2.xlarge' : 0.29,
'db.t2.2xlarge' : 0.58,

'db.m4.large' : 0.182,
'db.m4.xlarge' : 0.365,
'db.m4.2xlarge' : 0.73,
'db.m4.4xlarge' : 1.461,
'db.m4.10xlarge' : 3.654,
'db.m4.16xlarge' : 5.844,

'db.r4.large' : 0.25,
'db.r4.xlarge' : 0.50,
'db.r4.2xlarge' : 1.00,
'db.r4.4xlarge' : 2.00,
'db.r4.8xlarge' : 4.00,
'db.r4.16xlarge' : 8.00,

'db.r3.large' : 0.25,
'db.r3.xlarge' : 0.50,
'db.r3.2xlarge' : 0.995,
'db.r3.4xlarge' : 1.99,
'db.r3.8xlarge' : 3.98
}

# dict of us-east-1 rds oracle-se2 on demand prices as of 8/6/21
rds_oracle_se2_pricing_dict = {
'db.t3.micro' : 0.038,
'db.t3.small' : 0.075,
'db.t3.medium' : 0.15,
'db.t3.large' : 0.30,
'db.t3.xlarge' : 0.60,
'db.t3.2xlarge' : 1.20,

'db.m5.large' : 0.438,
'db.m5.xlarge' : 0.876,
'db.m5.2xlarge' : 1.752,
'db.m5.4xlarge' : 3.504,

'db.r5.large' : 0.482,
'db.r5.xlarge' : 0.964,
'db.r5.2xlarge' : 1.928,
'db.r5.4xlarge' : 3.856,

'db.t2.micro' : 0.038,
'db.t2.small' : 0.075,
'db.t2.medium' : 0.151,
'db.t2.large' : 0.301,
'db.t2.xlarge' : 0.604,
'db.t2.2xlarge' : 1.208,

'db.m4.large' : 0.442,
'db.m4.xlarge' : 0.885,
'db.m4.2xlarge' : 1.768,
'db.m4.4xlarge' : 3.537,

'db.r4.large' : 0.4892,
'db.r4.xlarge' : 0.9784,
'db.r4.2xlarge' : 1.9568,
'db.r4.4xlarge' : 3.9136,

'db.r3.large' : 0.489,
'db.r3.xlarge' : 0.978,
'db.r3.2xlarge' : 1.957,
'db.r3.4xlarge' : 3.913
}

# dict of us-east-1 rds oracle-se1 on demand prices as of 8/6/21
rds_oracle_se1_pricing_dict = {
'db.t3.micro' : 0.035,
'db.t3.small' : 0.07,
'db.t3.medium' : 0.14,
'db.t3.large' : 0.28,
'db.t3.xlarge' : 0.56,
'db.t3.2xlarge' : 1.12,

'db.m5.large' : 0.407,
'db.m5.xlarge' : 0.814,
'db.m5.2xlarge' : 1.628,
'db.m5.4xlarge' : 3.256,

'db.r5.large' : 0.448,
'db.r5.xlarge' : 0.896,
'db.r5.2xlarge' : 1.792,
'db.r5.4xlarge' : 3.584,

'db.t2.micro' : 0.035,
'db.t2.small' : 0.07,
'db.t2.medium' : 0.14,
'db.t2.large' : 0.28,

'db.m4.large' : 0.411,
'db.m4.xlarge' : 0.823,
'db.m4.2xlarge' : 1.645,
'db.m4.4xlarge' : 3.29,

'db.r3.large' : 0.455,
'db.r3.xlarge' : 0.91,
'db.r3.2xlarge' : 1.82,
'db.r3.4xlarge' : 3.64
}

# dict of us-east-1 rds sqlserver-se on demand prices as of 8/9/21
rds_sqlserver_se_pricing_dict = {
'db.t3.xlarge' : 1.044,
'db.t3.2xlarge' : 2.088,

'db.m5.large' : 0.977,
'db.m5.xlarge' : 1.224,
'db.m5.2xlarge' : 1.752,
'db.m5.4xlarge' : 3.504,
'db.m5.8xlarge' : 9.792,
'db.m5.12xlarge' : 14.688,
'db.m5.16xlarge' : 19.584,
'db.m5.24xlarge' : 29.376,

'db.m5d.large' : 0.993,
'db.m5d.xlarge' : 1.291,
'db.m5d.2xlarge' : 2.581,
'db.m5d.4xlarge' : 5.162,
'db.m5d.8xlarge' : 10.324,
'db.m5d.12xlarge' : 15.486,
'db.m5d.16xlarge' : 20.648,
'db.m5d.24xlarge' : 30.972,

'db.r5.large' : 1.02,
'db.r5.xlarge' : 1.52,
'db.r5.2xlarge' : 3.04,
'db.r5.4xlarge' : 6.08,
'db.r5.8xlarge' : 12.16,
'db.r5.12xlarge' : 18.24,
'db.r5.16xlarge' : 24.32,
'db.r5.24xlarge' : 36.48,

'db.r5b.large' : 1.19,
'db.r5b.xlarge' : 1.587,
'db.r5b.2xlarge' : 3.175,
'db.r5b.4xlarge' : 6.349,
'db.r5b.8xlarge' : 12.698,
'db.r5b.12xlarge' : 19.047,
'db.r5b.16xlarge' : 25.397,
'db.r5b.24xlarge' : 38.095,

'db.r5d.large' : 1.181,
'db.r5d.xlarge' : 1.571,
'db.r5d.2xlarge' : 3.142,
'db.r5d.4xlarge' : 6.283,
'db.r5d.8xlarge' : 12.566,
'db.r5d.12xlarge' : 18.85,
'db.r5d.16xlarge' : 25.133,
'db.r5d.24xlarge' : 37.699,

'db.z1d.large' : 1.251,
'db.z1d.xlarge' : 1.709,
'db.z1d.2xlarge' : 3.419,
'db.z1d.3xlarge' : 5.128,
'db.z1d.6xlarge' : 10.256,
'db.z1d.12xlarge' : 20.513,

'db.m4.large' : 0.977,
'db.m4.xlarge' : 1.224,
'db.m4.2xlarge' : 2.548,
'db.m4.4xlarge' : 5.047,
'db.m4.10xlarge' : 12.24,
'db.m4.16xlarge' : 19.584,

'db.r4.large' : 1.02,
'db.r4.xlarge' : 1.52,
'db.r4.2xlarge' : 3.04,
'db.r4.4xlarge' : 6.08,
'db.r4.8xlarge' : 12.16,
'db.r4.16xlarge' : 24.32,

'db.r3.large' : 1.02,
'db.r3.xlarge' : 1.52,
'db.r3.2xlarge' : 3.02,
'db.r3.4xlarge' : 6.04,
'db.r3.8xlarge' : 12.08
}

# dict of us-east-1 rds sqlserver-web on demand prices as of 8/9/21
rds_sqlserver_web_pricing_dict = {
'db.t3.small' : 0.139,
'db.t3.medium' : 0.166,
'db.t3.large' : 0.232,
'db.t3.xlarge' : 0.40,
'db.t3.2xlarge' : 0.80,

'db.m5.large' : 0.311,
'db.m5.xlarge' : 0.54,
'db.m5.2xlarge' : 1.102,
'db.m5.4xlarge' : 2.247,

'db.m5d.large' : 0.341,
'db.m5d.xlarge' : 0.598,
'db.m5d.2xlarge' : 1.194,
'db.m5d.4xlarge' : 2.388,

'db.r5.large' : 0.46,
'db.r5.xlarge' : 0.88,
'db.r5.2xlarge' : 1.76,
'db.r5.4xlarge' : 3.52,

'db.r5b.large' : 0.541,
'db.r5b.xlarge' : 0.963,
'db.r5b.2xlarge' : 1.923,
'db.r5b.4xlarge' : 3.847,

'db.r5d.large' : 0.532,
'db.r5d.xlarge' : 0.945,
'db.r5d.2xlarge' : 1.888,
'db.r5d.4xlarge' : 3.777,

'db.z1d.large' : 0.606,
'db.z1d.xlarge' : 1.092,
'db.z1d.2xlarge' : 2.182,
'db.z1d.3xlarge' : 3.274,

'db.t2.small' : 0.144,
'db.t2.medium' : 0.288,

'db.m4.large' : 0.311,
'db.m4.xlarge' : 0.54,
'db.m4.2xlarge' : 1.102,
'db.m4.4xlarge' : 2.247,

'db.r4.large' : 0.46,
'db.r4.xlarge' : 0.88,
'db.r4.2xlarge' : 1.76,

'db.r3.large' : 0.46,
'db.r3.xlarge' : 0.88,
'db.r3.2xlarge' : 1.80
}

# dict of us-east-1 docdb on demand prices as of 8/9/21
docdb_pricing_dict = {
'db.t3.medium' : 0.078,

'db.r5.large' : 0.277,
'db.r5.xlarge' : 0.554,
'db.r5.2xlarge' : 1.108,
'db.r5.4xlarge' : 2.216,
'db.r5.8xlarge' : 4.4312,
'db.r5.12xlarge' : 6.648,
'db.r5.16xlarge' : 8.8624,
'db.r5.24xlarge' : 13.296,

'db.r4.large' : 0.277,
'db.r4.xlarge' : 0.554,
'db.r4.2xlarge' : 1.108,
'db.r4.4xlarge' : 2.216,
'db.r4.8xlarge' : 4.432,
'db.r4.16xlarge' : 8.864
}

def getEC2Price(type):
    # return on demand hourly price
    return ec2_pricing_dict.get(type)

def getRDSPrice(engine, instanceClass, multi):
    if engine != 'aurora-mysql' and engine != 'aurora-postgresql' and engine != 'mariadb' and engine != 'mysql' and engine != 'postgres' and engine != 'oracle-se2' and engine != 'oracle-se1' and engine != 'sqlserver-se' and engine != 'sqlserver-web' and engine != 'docdb':
       return 'price not available'

    elif engine == 'aurora-mysql' or engine == 'aurora-postgresql': # aurora-mysql and aurora-postgresql instances have the same prices
        # return on demand hourly price
        price = rds_aurora_pricing_dict.get(instanceClass)
        if multi:
            return price*2
        else:
            return price

    elif engine == 'mariadb' or engine == 'mysql': # mariadb and mysql instances have the same prices
        # return on demand hourly price
        price = rds_mysql_pricing_dict.get(instanceClass)
        if multi:
            return price*2
        else:
            return price
    
    elif engine == 'postgres':
        # return on demand hourly price
        price = rds_postgres_pricing_dict.get(instanceClass)
        if multi:
            return price*2
        else:
            return price       

    elif engine == 'oracle-se2':
        # return on demand hourly price
        price = rds_oracle_se2_pricing_dict.get(instanceClass)
        if multi :
            return price*2
        else:
            return price

    elif engine == 'oracle-se1':
        # return on demand hourly price
        price = rds_oracle_se1_pricing_dict.get(instanceClass)
        if multi :
            return price*2
        else:
            return price
    
    elif engine == 'sqlserver-se':
        # return on demand hourly price
        price = rds_sqlserver_se_pricing_dict.get(instanceClass)
        if multi :
            return price*2
        else:
            return price

    elif engine == 'sqlserver-web':
        # return on demand hourly price
        price = rds_sqlserver_web_pricing_dict.get(instanceClass)
        return price
    
    elif engine == 'docdb':
        # return on demand hourly price
        price = docdb_pricing_dict.get(instanceClass)
        return price