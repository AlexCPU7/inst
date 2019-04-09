import React from 'react'
import Article from '../Article'
import './style.css'

export default function ArticleList({ articles }) {
    const articleElement = articles.map((article, index) =>
        <li key={article.id}>
            <Article article={article} defaultOpen={index === 0}/>
        </li>
    );
    return (
        <ul className='article-list__li'>
            {articleElement}
        </ul>
    )
}