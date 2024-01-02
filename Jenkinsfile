pipeline{

	agent {label 'linux'}

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
	}

	stages {
	    
	    stage('gitclone') {

			steps {
				git 'https://github.com/Samarth-Kumar-Samal/Stock-Prediction-using-FbProphet-Streamlit-Yfinance.git'
			}
		}

		stage('Build') {

			steps {
				sh 'docker build -t samarthkumarsamal1606/stock-prediction-app:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push samarthkumarsamal1606/stock-prediction-app:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}