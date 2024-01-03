pipeline {
    agent any
    
    environment {
        registryRepo = "samarthkumarsamal1606/test-stock-app"
        registry = "https://registry.hub.docker.com"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                script {
                    git branch: 'refs/heads/main', url: 'https://github.com/Samarth-Kumar-Samal/Stock-Prediction-using-FbProphet-Streamlit-Yfinance.git'
                }
            }
        }
        
        stage('Build Image') {
            steps {
                script {
                    def img = "${registryRepo}:${env.BUILD_NUMBER}"
                    println("${img}")
                    dockerImage = docker.build(img)
                }
            }
        }
        
        stage('Push Image to DockerHub') {
            steps {
                script {
                    docker.withRegistry(registry, registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
