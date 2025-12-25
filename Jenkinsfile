
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t username/devops-demo:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                    docker login -u $USER -p $PASS
                    docker push username/devops-demo:latest
                    '''
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                docker stop demo || true
                docker rm demo || true
                docker run -d --name demo -p 5000:5000 username/devops-demo:latest
                '''
            }
        }
    }
}


