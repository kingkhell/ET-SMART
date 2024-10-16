<?php
require 'vendor/autoload.php'; // include Composer's autoloader

$client = new MongoDB\Client("mongodb://localhost:27017");

$database = $client->selectDatabase('testdb'); 
$collection = $database->selectCollection('users'); 


$insertResult = $collection->insertOne([
    'name' => 'John Doe',
    'email' => 'john@example.com'
]);

echo "Inserted with Object ID '{$insertResult->getInsertedId()}'";

$document = $collection->findOne(['name' => 'John Doe']);
echo "Found document: " . json_encode($document);
?>
