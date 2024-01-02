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
                    sh "docker build -t ${dockerImage} ."
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh """
                        docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                        """
                    }
                    sh "docker push ${dockerImage}"
                }
            }
        }
    }
}