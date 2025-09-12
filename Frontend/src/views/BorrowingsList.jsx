import React, { useEffect, useState } from 'react';

export default function BorrowingsList() {
  const [borrowings, setBorrowings] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL + '/borrowings/?overdue=true')
      .then(res => res.json())
      .then(data => setBorrowings(data))
      .catch(err => alert('Failed to load borrowings.'));
  }, []);

  return (
    <div>
      <h2>Overdue Borrowings</h2>
      {borrowings.map(b => (
        <div key={b.id}>
          Book ID: {b.book}, Customer ID: {b.customer}<br/>
          Due: {b.due_date}<br/><br/>
        </div>
      ))}
    </div>
  );
}
