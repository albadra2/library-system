import React, { useEffect, useState } from 'react';

export default function AuthorPage() {
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/authors/')
      .then(res => res.json())
      .then(data => setAuthors(data))
      .catch(err => alert('Failed to load authors.'));
  }, []);

  return (
    <div>
      <h2>Authors</h2>
      {authors.map(author => (
        <div key={author.id}>
          <strong>{author.name}</strong><br/>
          Bio: {author.biography}<br/><br/>
        </div>
      ))}
    </div>
  );
}
