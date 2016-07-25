class AsciiDocument:

    def __init__(self, documentheading):

        self._heading = documentheading
        self._authors = []
        self._emails = []
        self._revisions = []
        self._sections = []

        return

    def GetAuthors(self):

        return self._authors

    def AddAuthor(self, author):

        self._authors.append(author)

        return

    def RemoveAuthor(self, author):

        self._authors.remove(author)

        return

    def GetEmails(self):

        return self._emails

    def AddEmail(self, email):

        self._emails.append(email)

        return

    def RemoveEmail(self, email):

        self._emails.remove(email)

        return

    def GetRevisions(self):

        return self._revisions

    def AddRevision(self, version, date):

        self._revisions.append((version, date))

        return

    def GenerateAsciiDoc(self):

        asciidoccontent = ""

        asciidoccontent += str.format("{0}\n{1}\n", self._heading, "=" * len(self._heading))

        for item in self._authors:

            asciidoccontent += str.format(":Author: {0}\n", item)

        for item in self._emails:

            asciidoccontent += str.format(":Email: <{0}>\n", item)

        for item in self._revisions:

            asciidoccontent += str.format(":Date: {0}\n:Revision: {1}", item[1], item[0])

        return asciidoccontent