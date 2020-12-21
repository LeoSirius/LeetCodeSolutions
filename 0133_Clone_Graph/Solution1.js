
function Node(val, neighbors) {
  this.val = val === undefined ? 0 : val;
  this.neighbors = neighbors === undefined ? [] : neighbors;
};

/**
* @param {Node} node
* @return {Node}
*/
var cloneGraph = function(node) {
   let visited = Array().fill(false, 0, 101);
   var clone = function(node) {
     if (!node)
       return null;
     let newNode = new Node(node.val);
     visited[newNode.val] = newNode;
     for (neighborNode of node.neighbors) {
       if (visited[neighborNode.val]) {
         newNode.neighbors.push(visited[neighborNode.val]);
       } else {
         newNode.neighbors.push(clone(neighborNode));
       }
     }
     return newNode;
   }
   return clone(node);
};

// 此题不测