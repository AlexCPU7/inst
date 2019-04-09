import React, {Component} from 'react'

class Article extends Component {
    // state = {
    //     isOpen: false
    // };
    constructor(props){
        super(props);

        this.state = {
            isOpen: props.defaultOpen
        }
    }

    componentWillMount() {
        /* вызывается до появления компонента в DOM */
        console.log('use componentWillMount')
    }
    /* вызывается render() */
    componentDidMount() {
        /* вызывается после появления компонента в DOM */
        console.log('use componentDidMount')
    }

    componentWillReceiveProps(nextProps, nextContext) {
        /* обновляет компонент */
        console.log('use componentDidMount')
    }

    render() {
        const {article} = this.props;
        const style = {width: '90%'};
        const body = this.state.isOpen && <div className='card-text'>{article.text}</div>;
        return (
            <div className='card mx-auto' style={style}>
                <div className='card-header'>
                    <h2>{article.title}</h2>
                    <button onClick={this.handleClick}
                            className='btn btn-primary btn-lg'>
                        {this.state.isOpen ? 'Close' : 'Open'}
                    </button>
                </div>
                <div className='card-body'>
                    <h6 className='card-subtitle text-muted'>
                        create date: {(new Date(article.date)).toDateString()}
                    </h6>
                    <div>{body}</div>
                </div>
            </div>
        )
    }

    handleClick = () => {
        console.log('cliick');
        this.setState({
            isOpen: !this.state.isOpen
        })
    }
}

export default Article