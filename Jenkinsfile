pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('dockerhub_id')
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/Samarth-Kumar-Samal/Stock-Prediction-using-FbProphet-Streamlit-Yfinance.git']]])
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = 'samarthkumarsamal1606/stock-prediction-app'
                    sh 'docker build -t ${dockerImage} .'

                    // Set environment variables for the Docker login command
                    withEnv(["DOCKER_USERNAME=${DOCKER_HUB_CREDENTIALS_USR}", "DOCKER_PASSWORD=${DOCKER_HUB_CREDENTIALS_PSW}"]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    }

                    sh 'docker push ${dockerImage}'
                }
            }
        }
    }
}
