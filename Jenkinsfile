pipeline{
    agent {
        docker { image 'python' }
    }
    environment{
        dockerhub = credentials("dockerhub_luna4444")
    }

    stages {
        stage('Installing Dependencies...') {
            steps {
                sh 'Will start to fail...'
                sh 'pip install -r requirements.txt'
                sh 'python manage.py test'


                sh 'All tests passed successfully!'
            }
        }
        stage('Build Image...'){
            steps{
                sh 'docker build -t todo_app_jenkins .'
            }
    }
        stage("Start Pushing to Docker Hub..."){
                steps {
                sh 'docker tag todo_app_jenkins $dockerhub_USR/sample_repo:todo_app_jenkins'
                sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'

                sh 'docker push $dockerhub_USR/sample_repo:todo_app_jenkins'
                }
        }
    }

}
