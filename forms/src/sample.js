import React from "react";
import { useState } from "react";

function AddEdit() {
    const [rows,setRows] = React.useState([
        { name: 'Alice', email: 'alice@example.com', editing: false },
        { name: 'Michael', email: 'michael@example.com', editing: false },
        { name: 'Emily', email: 'emily@example.com', editing: false },
        { name: 'David', email: 'david@example.com', editing: false },
        { name: 'Sarah', email: 'sarah@example.com', editing: false },
        { name: 'Daniel', email: 'daniel@example.com', editing: false },
        { name: 'Olivia', email: 'olivia@example.com', editing: false },
        { name: 'Andrew', email: 'andrew@example.com', editing: false }
    ]);

    const editRow = (row) => {
        const updatedRows = rows.map((r) => {
            if (r === row) {
                return { ...r, editing: true };
            }
            return r;
        });
        setRows(updatedRows);
    };

    const saveRow = (row) => {
        const updatedRows = rows.map((r) => {
            if (r === row) {
                return { ...r, editing: false };
            }
            return r;
        });
        setRows(updatedRows);
    };

    const deleteRow = (index) => {
        const updatedRows = [...rows];
        updatedRows.splice(index, 1);
        setRows(updatedRows);
    };

    const addRow = () => {
        const newRows = [...rows, { name: '', email: '', editing: true }];
        setRows(newRows);
    };

    return (
        <div className='container'>
            <h3>React Js Table with edit and delete button</h3>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {rows.map((row, index) => (
                        <tr key={index}>
                            {!row.editing && <td>{row.name}</td>}
                            {!row.editing && <td>{row.email}</td>}
                            {row.editing && <td><input type="text" value={row.name} onChange={(e) => {
                                const updatedRows = [...rows];
                                updatedRows[index].name = e.target.value;
                                setRows(updatedRows);
                            }} /></td>}
                            {row.editing && <td><input type="email" value={row.email} onChange={(e) => {
                                const updatedRows = [...rows];
                                updatedRows[index].email = e.target.value;
                                setRows(updatedRows);
                            }} /></td>}
                            <td>
                                {!row.editing && <button className="edit-button" onClick={() => editRow(row)}>Edit</button>}
                                {row.editing && <button className="save-button" onClick={() => saveRow(row)}>Save</button>}
                                <button className="delete-button" onClick={() => deleteRow(index)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <button className="add-button" onClick={addRow}>Add Row</button>
        </div>
            );
}

export default AddEdit