from modeller import *
env = Environ()
aln = Alignment(env)
for (pdb, chain) in (('1b8p', 'A'), ('1bdm', 'A'), ('1civ', 'A'),
                     ('5mdh', 'A'), ('7mdh', 'A'), ('1smk', 'A')):
                     m = Model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
                     aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
                     aln.malign()
                     aln.malign3d()
                     aln.compare_structures()
                     aln.id_table(matrix_file='family.mat')
                     env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)

# {
#   "taskDefinitionArn": "",
#   "containerDefinitions": [
#     {
#       "name": "api",
#       "image": "",
#       "cpu": 0,
#       "portMappings": [
#         {
#           "name": "api-80-tcp",
#           "containerPort": 80,
#           "hostPort": 80,
#           "protocol": "tcp",
#           "appProtocol": "http"
#         }
#       ],
#       "essential": true,
#       "environment": [
#         {
#           "name": "VERSION",
#           "value": "1.0"
#         },
#         {
#           "name": "APP_RUNTIME_ENV",
#           "value": "UAT"
#         },
#         {
#           "name": "ASPNETCORE_HTTP_PORTS",
#           "value": "80"
#         },
#         {
#           "name": "AWS_REGION",
#           "value": "af-south-1"
#         },
#         {
#           "name": "AWS_BUCKET",
#           "value": ""
#         },
#         {
#           "name": "CONTENT_URL",
#           "value": ""
#         },
#         {
#           "name": "APP_URL",
#           "value": ""
#         },
#         {
#           "name": "OPEN_AI_MODEL",
#           "value": "gpt-3.5-turbo-16k"
#         }
#       ],
#       "environmentFiles": [],
#       "mountPoints": [],
#       "volumesFrom": [],
#       "secrets": [
#         {
#           "name": "CONNECTION_STRING",
#           "valueFrom": ""
#         },
#         {
#           "name": "AWS_ACCESS_KEY",
#           "valueFrom": ""
#         },
#         {
#           "name": "AWS_ACCESS_SECRET",
#           "valueFrom": ""
#         },
#         {
#           "name": "OPEN_AI_KEY",
#           "valueFrom": ""
#         },
#         {
#           "name": "SENDGRID_API_KEY",
#           "valueFrom": ""
#         },
#         {
#           "name": "RECAPTCHA_SECRET_KEY",
#           "valueFrom": ""
#         }
#       ],
#       "logConfiguration": {
#         "logDriver": "awslogs",
#         "options": {
#           "awslogs-create-group": "true",
#           "awslogs-group": "",
#           "awslogs-region": "af-south-1",
#           "awslogs-stream-prefix": "ecs"
#         }
#       }
#     }
#   ],
#   "family": "",
#   "executionRoleArn": "",
#   "networkMode": "awsvpc",
#   "revision": 1,
#   "volumes": [],
#   "status": "ACTIVE",
#   "requiresAttributes": [
#     {
#       "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
#     },
#     {
#       "name": "ecs.capability.execution-role-awslogs"
#     },
#     {
#       "name": "com.amazonaws.ecs.capability.ecr-auth"
#     },
#     {
#       "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
#     },
#     {
#       "name": "ecs.capability.secrets.asm.environment-variables"
#     },
#     {
#       "name": "ecs.capability.execution-role-ecr-pull"
#     },
#     {
#       "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
#     },
#     {
#       "name": "ecs.capability.task-eni"
#     },
#     {
#       "name": "com.amazonaws.ecs.capability.docker-remote-api.1.29"
#     }
#   ],
#   "placementConstraints": [],
#   "compatibilities": ["EC2", "FARGATE"],
#   "requiresCompatibilities": ["FARGATE"],
#   "cpu": "1024",
#   "memory": "2048",
#   "runtimePlatform": {
#     "cpuArchitecture": "X86_64",
#     "operatingSystemFamily": "LINUX"
#   },
#   "registeredAt": "2023-03-21T19:53:44.968Z",
#   "registeredBy": "",
#   "tags": []
# }
