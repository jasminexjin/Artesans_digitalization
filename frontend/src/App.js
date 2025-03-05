import { useState } from "react";
import { Button, Input, Textarea, Card, CardContent } from "@/components/ui";
import { BarcodeScanner } from "@/components/BarcodeScanner";
import { Table } from "@/components/ui/table";

export default function BarcodeApp() {
  const [scannedCode, setScannedCode] = useState("");
  const [name, setName] = useState("");
  const [comment, setComment] = useState("");
  const [entries, setEntries] = useState([]);
  const [error, setError] = useState("");

  const handleScan = (code) => {
    if (code) {
      setScannedCode(code);
      setError("");
    } else {
      setError("Invalid barcode. Please scan again.");
    }
  };

  const handleSubmit = () => {
    if (scannedCode && name.trim() && comment.trim()) {
      setEntries([...entries, { code: scannedCode, name, comment }]);
      setScannedCode("");
      setName("");
      setComment("");
    } else {
      setError("Please fill in all fields before submitting.");
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Barcode Scanner & Input</h1>
      <BarcodeScanner onScan={handleScan} />
      {scannedCode && (
        <Card className="mt-4 p-4">
          <CardContent>
            <p className="mb-2">Scanned Code: <strong>{scannedCode}</strong></p>
            <Input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter name"
              className="mb-2"
            />
            <Textarea
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              placeholder="Enter comment. 'NA'if not applicable."
              className="mb-2"
            />
            <Button onClick={handleSubmit}>Save Entry</Button>
          </CardContent>
        </Card>
      )}

      {entries.length > 0 && (
        <Card className="mt-6 p-4">
          <CardContent>
            <h2 className="text-xl font-semibold mb-2">Saved Entries</h2>
            <Table>
              <thead>
                <tr>
                  <th>Barcode</th>
                  <th>Name</th>
                  <th>Comment</th>
                </tr>
              </thead>
              <tbody>
                {entries.map((entry, index) => (
                  <tr key={index}>
                    <td>{entry.code}</td>
                    <td>{entry.name}</td>
                    <td>{entry.comment}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
