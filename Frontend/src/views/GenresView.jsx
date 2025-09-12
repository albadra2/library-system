import React, { useEffect, useState } from 'react';

export default function GenresView() {
  const [genres, setGenres] = useState([]);
  const [selected, setSelected] = useState('');
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/genres/')
      .then(res => res.json())
      .then(data => setGenres(data))
      .catch(err => alert('Failed to load genres.'));
  }, []);

  useEffect(() => {
    if (selected) {
      fetch(process.env.REACT_APP_API_URL + `/books/?genre=${selected}`)
        .then(res => res.json())
        .then(data => setBooks(data))
        .catch(err => alert('Failed to load books.'));
    }
  }, [selected]);

  return (
    <div>
      <h2>Genres</h2>
      <select onChange={e => setSelected(e.target.value)}>
        <option value="">Choose a Genre</option>
        {genres.map(g => (
          <option key={g.id} value={g.id}>{g.name}</option>
        ))}
      </select>
      <div>
        {books.map(book => (
          <div key={book.id}>{book.title}</div>
        ))}
      </div>
    </div>
  );
}
