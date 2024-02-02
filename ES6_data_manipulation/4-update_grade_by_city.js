export default function updateStudentGradeByCity(array, city, newGrades) {
  const stundentsByCity = array.filter((ele) => ele.location === city);
  const ids = newGrades.map((ele) => ele.studentId);
  for (const student of stundentsByCity) {
    if (ids.includes(student.id)) {
      for (const grade of newGrades) {
        if (grade.studentId === student.id) {
          student.grade = grade.grade;
        }
      }
    } else {
      student.grade = 'N/A';
    }
  }
  return stundentsByCity;
}
