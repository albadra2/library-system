import React, { useEffect, useState } from 'react';

export default function HomePage() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/books/')
      .then(res => res.json())
      .then(data => setBooks(data))
      .catch(err => alert('Failed to load books.'));
  }, []);

  return (
    <div>
      <h2>All Books</h2>
      {books.map(book => (
        <div key={book.id}>
          <strong>{book.title}</strong><br/>
          Published: {book.published_date}<br/>
          ISBN: {book.isbn}<br/><br/>
        </div>
      ))}
    </div>
  );
}
