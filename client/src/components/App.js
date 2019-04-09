import React, {Component} from 'react'
import ArticleList from './ArticleList'
import articles from '../fixtures'
import 'bootstrap/dist/css/bootstrap.css'

class App extends Component {
    render() {
        return (
            <div className='container'>
                <div className='jumbotron'>
                    <h1 className='display-3'>App name</h1>
                </div>
                <ArticleList articles={articles} foo='test' is_flag={true} is_flag_true/>
            </div>
        )
    }
}

export default App