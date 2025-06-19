"""
Scripture database population script
Populates the database with comprehensive LDS scripture data
"""

from src.models.user import Scripture, db
import json

def populate_scriptures():
    """Populate database with comprehensive scripture data"""
    
    # Sample comprehensive scripture data
    scriptures_data = [
        # Old Testament - Genesis
        {"book": "Genesis", "chapter": 1, "verse": 1, "text": "In the beginning God created the heaven and the earth.", "collection": "Old Testament"},
        {"book": "Genesis", "chapter": 1, "verse": 27, "text": "So God created man in his own image, in the image of God created he him; male and female created he them.", "collection": "Old Testament"},
        {"book": "Genesis", "chapter": 2, "verse": 7, "text": "And the Lord God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.", "collection": "Old Testament"},
        
        # Psalms
        {"book": "Psalms", "chapter": 23, "verse": 1, "text": "The Lord is my shepherd; I shall not want.", "collection": "Old Testament"},
        {"book": "Psalms", "chapter": 23, "verse": 4, "text": "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.", "collection": "Old Testament"},
        {"book": "Psalms", "chapter": 46, "verse": 10, "text": "Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth.", "collection": "Old Testament"},
        
        # Isaiah
        {"book": "Isaiah", "chapter": 55, "verse": 8, "text": "For my thoughts are not your thoughts, neither are your ways my ways, saith the Lord.", "collection": "Old Testament"},
        {"book": "Isaiah", "chapter": 55, "verse": 9, "text": "For as the heavens are higher than the earth, so are my ways higher than your ways, and my thoughts than your thoughts.", "collection": "Old Testament"},
        {"book": "Isaiah", "chapter": 40, "verse": 31, "text": "But they that wait upon the Lord shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.", "collection": "Old Testament"},
        
        # Jeremiah
        {"book": "Jeremiah", "chapter": 29, "verse": 11, "text": "For I know the thoughts that I think toward you, saith the Lord, thoughts of peace, and not of evil, to give you an expected end.", "collection": "Old Testament"},
        
        # New Testament - Matthew
        {"book": "Matthew", "chapter": 5, "verse": 16, "text": "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.", "collection": "New Testament"},
        {"book": "Matthew", "chapter": 6, "verse": 33, "text": "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.", "collection": "New Testament"},
        {"book": "Matthew", "chapter": 11, "verse": 28, "text": "Come unto me, all ye that labour and are heavy laden, and I will give you rest.", "collection": "New Testament"},
        {"book": "Matthew", "chapter": 28, "verse": 19, "text": "Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost:", "collection": "New Testament"},
        
        # John
        {"book": "John", "chapter": 3, "verse": 16, "text": "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.", "collection": "New Testament"},
        {"book": "John", "chapter": 14, "verse": 6, "text": "Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me.", "collection": "New Testament"},
        {"book": "John", "chapter": 8, "verse": 32, "text": "And ye shall know the truth, and the truth shall make you free.", "collection": "New Testament"},
        {"book": "John", "chapter": 15, "verse": 13, "text": "Greater love hath no man than this, that a man lay down his life for his friends.", "collection": "New Testament"},
        
        # Romans
        {"book": "Romans", "chapter": 8, "verse": 28, "text": "And we know that all things work together for good to them that love God, to them who are the called according to his purpose.", "collection": "New Testament"},
        {"book": "Romans", "chapter": 10, "verse": 17, "text": "So then faith cometh by hearing, and hearing by the word of God.", "collection": "New Testament"},
        
        # 1 Corinthians
        {"book": "1 Corinthians", "chapter": 13, "verse": 4, "text": "Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up,", "collection": "New Testament"},
        {"book": "1 Corinthians", "chapter": 13, "verse": 13, "text": "And now abideth faith, hope, charity, these three; but the greatest of these is charity.", "collection": "New Testament"},
        {"book": "1 Corinthians", "chapter": 10, "verse": 13, "text": "There hath no temptation taken you but such as is common to man: but God is faithful, who will not suffer you to be tempted above that ye are able; but will with the temptation also make a way to escape, that ye may be able to bear it.", "collection": "New Testament"},
        
        # Philippians
        {"book": "Philippians", "chapter": 4, "verse": 13, "text": "I can do all things through Christ which strengtheneth me.", "collection": "New Testament"},
        {"book": "Philippians", "chapter": 4, "verse": 19, "text": "But my God shall supply all your need according to his riches in glory by Christ Jesus.", "collection": "New Testament"},
        
        # Hebrews
        {"book": "Hebrews", "chapter": 11, "verse": 1, "text": "Now faith is the substance of things hoped for, the evidence of things not seen.", "collection": "New Testament"},
        {"book": "Hebrews", "chapter": 11, "verse": 6, "text": "But without faith it is impossible to please him: for he that cometh to God must believe that he is, and that he is a rewarder of them that diligently seek him.", "collection": "New Testament"},
        
        # James
        {"book": "James", "chapter": 1, "verse": 5, "text": "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him.", "collection": "New Testament"},
        {"book": "James", "chapter": 2, "verse": 17, "text": "Even so faith, if it hath not works, is dead, being alone.", "collection": "New Testament"},
        
        # Book of Mormon - 1 Nephi
        {"book": "1 Nephi", "chapter": 3, "verse": 7, "text": "And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them.", "collection": "Book of Mormon"},
        {"book": "1 Nephi", "chapter": 19, "verse": 23, "text": "And I did read many things unto them which were written in the books of Moses; but that I might more fully persuade them to believe in the Lord their Redeemer I did read unto them that which was written by the prophet Isaiah; for I did liken all scriptures unto us, that it might be for our profit and learning.", "collection": "Book of Mormon"},
        
        # 2 Nephi
        {"book": "2 Nephi", "chapter": 2, "verse": 25, "text": "Adam fell that men might be; and men are, that they might have joy.", "collection": "Book of Mormon"},
        {"book": "2 Nephi", "chapter": 25, "verse": 26, "text": "And we talk of Christ, we rejoice in Christ, we preach of Christ, we prophesy of Christ, and we write according to our prophecies, that our children may know to what source they may look for a remission of their sins.", "collection": "Book of Mormon"},
        {"book": "2 Nephi", "chapter": 32, "verse": 3, "text": "Angels speak by the power of the Holy Ghost; wherefore, they speak the words of Christ. Wherefore, I said unto you, feast upon the words of Christ; for behold, the words of Christ will tell you all things what ye should do.", "collection": "Book of Mormon"},
        
        # Mosiah
        {"book": "Mosiah", "chapter": 2, "verse": 17, "text": "And behold, I tell you these things that ye may learn wisdom; that ye may learn that when ye are in the service of your fellow beings ye are only in the service of your God.", "collection": "Book of Mormon"},
        {"book": "Mosiah", "chapter": 3, "verse": 19, "text": "For the natural man is an enemy to God, and has been from the fall of Adam, and will be, forever and ever, unless he yields to the enticings of the Holy Spirit, and putteth off the natural man and becometh a saint through the atonement of Christ the Lord, and becometh as a child, submissive, meek, humble, patient, full of love, willing to submit to all things which the Lord seeth fit to inflict upon him, even as a child doth submit to his father.", "collection": "Book of Mormon"},
        
        # Alma
        {"book": "Alma", "chapter": 32, "verse": 21, "text": "And now as I said concerning faith—faith is not to have a perfect knowledge of things; therefore if ye have faith ye hope for things which are not seen, which are true.", "collection": "Book of Mormon"},
        {"book": "Alma", "chapter": 37, "verse": 6, "text": "Now ye may suppose that this is foolishness in me; but behold I say unto you, that by small and simple things are great things brought to pass; and small means in many instances doth confound the wise.", "collection": "Book of Mormon"},
        {"book": "Alma", "chapter": 37, "verse": 35, "text": "O, remember, my son, and learn wisdom in thy youth; yea, learn in thy youth to keep the commandments of God.", "collection": "Book of Mormon"},
        {"book": "Alma", "chapter": 41, "verse": 10, "text": "Do not suppose, because it has been spoken concerning restoration, that ye shall be restored from sin to happiness. Behold, I say unto you, wickedness never was happiness.", "collection": "Book of Mormon"},
        
        # Helaman
        {"book": "Helaman", "chapter": 5, "verse": 12, "text": "And now, my sons, remember, remember that it is upon the rock of our Redeemer, who is Christ, the Son of God, that ye must build your foundation; that when the devil shall send forth his mighty winds, yea, his shafts in the whirlwind, yea, when all his hail and his mighty storm shall beat upon you, it shall have no power over you to drag you down to the gulf of misery and endless wo, because of the rock upon which ye are built, which is a sure foundation, a foundation whereon if men build they cannot fall.", "collection": "Book of Mormon"},
        
        # 3 Nephi
        {"book": "3 Nephi", "chapter": 11, "verse": 29, "text": "For verily, verily I say unto you, he that hath the spirit of contention is not of me, but is of the devil, who is the father of contention, and he stirreth up the hearts of men to contend with anger, one with another.", "collection": "Book of Mormon"},
        {"book": "3 Nephi", "chapter": 27, "verse": 20, "text": "Now this is the commandment: Repent, all ye ends of the earth, and come unto me and be baptized in my name, that ye may be sanctified by the reception of the Holy Ghost, that ye may stand spotless before me at the last day.", "collection": "Book of Mormon"},
        
        # Ether
        {"book": "Ether", "chapter": 12, "verse": 6, "text": "And now, I, Moroni, would speak somewhat concerning these things; I would show unto the world that faith is things which are hoped for and not seen; wherefore, dispute not because ye see not, for ye receive no witness until after the trial of your faith.", "collection": "Book of Mormon"},
        {"book": "Ether", "chapter": 12, "verse": 27, "text": "And if men come unto me I will show unto them their weakness. I give unto men weakness that they may be humble; and my grace is sufficient for all men that humble themselves before me; for if they humble themselves before me, and have faith in me, then will I make weak things become strong unto them.", "collection": "Book of Mormon"},
        
        # Moroni
        {"book": "Moroni", "chapter": 7, "verse": 41, "text": "And what is it that ye shall hope for? Behold I say unto you that ye shall have hope through the atonement of Christ and the power of his resurrection, to be raised unto life eternal, and this because of your faith in him according to the promise.", "collection": "Book of Mormon"},
        {"book": "Moroni", "chapter": 7, "verse": 45, "text": "And charity suffereth long, and is kind, and envieth not, and is not puffed up, seeketh not her own, is not easily provoked, thinketh no evil, and rejoiceth not in iniquity but rejoiceth in the truth, beareth all things, believeth all things, hopeth all things, endureth all things.", "collection": "Book of Mormon"},
        {"book": "Moroni", "chapter": 10, "verse": 4, "text": "And when ye shall receive these things, I would exhort you that ye would ask God, the Eternal Father, in the name of Christ, if these things are not true; and if ye shall ask with a sincere heart, with real intent, having faith in Christ, he will manifest the truth of it unto you, by the power of the Holy Ghost.", "collection": "Book of Mormon"},
        {"book": "Moroni", "chapter": 10, "verse": 5, "text": "And by the power of the Holy Ghost ye may know the truth of all things.", "collection": "Book of Mormon"},
        
        # Doctrine and Covenants
        {"book": "Doctrine and Covenants", "chapter": 1, "verse": 38, "text": "What I the Lord have spoken, I have spoken, and I excuse not myself; and though the heavens and the earth pass away, my word shall not pass away, but shall all be fulfilled, whether by mine own voice or by the voice of my servants, it is the same.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 6, "verse": 36, "text": "Look unto me in every thought; doubt not, fear not.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 8, "verse": 2, "text": "Yea, behold, I will tell you in your mind and in your heart, by the Holy Ghost, which shall come upon you and which shall dwell in your heart.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 18, "verse": 10, "text": "Remember the worth of souls is great in the sight of God;", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 18, "verse": 15, "text": "And if it so be that you should labor all your days in crying repentance unto this people, and bring, save it be one soul unto me, how great shall be your joy with him in the kingdom of my Father!", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 25, "verse": 12, "text": "For my soul delighteth in the song of the heart; yea, the song of the righteous is a prayer unto me, and it shall be answered with a blessing upon their heads.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 58, "verse": 27, "text": "Verily I say, men should be anxiously engaged in a good cause, and do many things of their own free will, and bring to pass much righteousness;", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 76, "verse": 22, "text": "And now, after the many testimonies which have been given of him, this is the testimony, last of all, which we give of him: That he lives!", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 84, "verse": 33, "text": "For whoso is faithful unto the obtaining these two priesthoods of which I have spoken, and the magnifying their calling, are sanctified by the Spirit unto the renewing of their bodies.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 88, "verse": 67, "text": "And if your eye be single to my glory, your whole bodies shall be filled with light, and there shall be no darkness in you; and that body which is filled with light comprehendeth all things.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 121, "verse": 7, "text": "My son, peace be unto thy soul; thine adversity and thine afflictions shall be but a small moment;", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 121, "verse": 45, "text": "Let thy bowels also be full of charity towards all men, and to the household of faith, and let virtue garnish thy thoughts unceasingly; then shall thy confidence wax strong in the presence of God; and the doctrine of the priesthood shall distil upon thy soul as the dews from heaven.", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 130, "verse": 20, "text": "There is a law, irrevocably decreed in heaven before the foundations of this world, upon which all blessings are predicated—", "collection": "Doctrine and Covenants"},
        {"book": "Doctrine and Covenants", "chapter": 130, "verse": 21, "text": "And when we obtain any blessing from God, it is by obedience to that law upon which it is predicated.", "collection": "Doctrine and Covenants"},
        
        # Pearl of Great Price - Moses
        {"book": "Moses", "chapter": 1, "verse": 39, "text": "For behold, this is my work and my glory—to bring to pass the immortality and eternal life of man.", "collection": "Pearl of Great Price"},
        {"book": "Moses", "chapter": 7, "verse": 18, "text": "And the Lord called his people Zion, because they were of one heart and one mind, and dwelt in righteousness; and there was no poor among them.", "collection": "Pearl of Great Price"},
        
        # Abraham
        {"book": "Abraham", "chapter": 3, "verse": 22, "text": "Now the Lord had shown unto me, Abraham, the intelligences that were organized before the world was; and among all these there were many of the noble and great ones;", "collection": "Pearl of Great Price"},
        {"book": "Abraham", "chapter": 3, "verse": 23, "text": "And God saw these souls that they were good, and he stood in the midst of them, and he said: These I will make my rulers; for he stood among those that were spirits, and he saw that they were good; and he said unto me: Abraham, thou art one of them; thou wast chosen before thou wast born.", "collection": "Pearl of Great Price"},
        
        # Joseph Smith—History
        {"book": "Joseph Smith—History", "chapter": 1, "verse": 15, "text": "I saw a pillar of light exactly over my head, above the brightness of the sun, which descended gradually until it fell upon me.", "collection": "Pearl of Great Price"},
        {"book": "Joseph Smith—History", "chapter": 1, "verse": 17, "text": "When the light rested upon me I saw two Personages, whose brightness and glory defy all description, standing above me in the air. One of them spake unto me, calling me by name and said, pointing to the other—This is My Beloved Son. Hear Him!", "collection": "Pearl of Great Price"},
        
        # Articles of Faith
        {"book": "Articles of Faith", "chapter": 1, "verse": 1, "text": "We believe in God, the Eternal Father, and in His Son, Jesus Christ, and in the Holy Ghost.", "collection": "Pearl of Great Price"},
        {"book": "Articles of Faith", "chapter": 1, "verse": 13, "text": "We believe in being honest, true, chaste, benevolent, virtuous, and in doing good to all men; indeed, we may say that we follow the admonition of Paul—We believe all things, we hope all things, we have endured many things, and hope to be able to endure all things. If there is anything virtuous, lovely, or of good report or praiseworthy, we seek after these things.", "collection": "Pearl of Great Price"},
        
        # Additional verses with common search terms
        {"book": "Psalms", "chapter": 119, "verse": 105, "text": "Thy word is a lamp unto my feet, and a light unto my path.", "collection": "Old Testament"},
        {"book": "Proverbs", "chapter": 3, "verse": 5, "text": "Trust in the Lord with all thine heart; and lean not unto thine own understanding.", "collection": "Old Testament"},
        {"book": "Proverbs", "chapter": 3, "verse": 6, "text": "In all thy ways acknowledge him, and he shall direct thy paths.", "collection": "Old Testament"},
        {"book": "Ecclesiastes", "chapter": 3, "verse": 1, "text": "To every thing there is a season, and a time to every purpose under the heaven:", "collection": "Old Testament"},
        {"book": "Isaiah", "chapter": 1, "verse": 18, "text": "Come now, and let us reason together, saith the Lord: though your sins be as scarlet, they shall be as white as snow; though they be red like crimson, they shall be as wool.", "collection": "Old Testament"},
        {"book": "Matthew", "chapter": 7, "verse": 7, "text": "Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you:", "collection": "New Testament"},
        {"book": "Luke", "chapter": 2, "verse": 52, "text": "And Jesus increased in wisdom and stature, and in favour with God and man.", "collection": "New Testament"},
        {"book": "1 John", "chapter": 4, "verse": 8, "text": "He that loveth not knoweth not God; for God is love.", "collection": "New Testament"},
        {"book": "Revelation", "chapter": 3, "verse": 20, "text": "Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me.", "collection": "New Testament"},
        
        # More verses with "hand" for testing
        {"book": "Isaiah", "chapter": 41, "verse": 10, "text": "Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.", "collection": "Old Testament"},
        {"book": "Psalms", "chapter": 139, "verse": 10, "text": "Even there shall thy hand lead me, and thy right hand shall hold me.", "collection": "Old Testament"},
        {"book": "Matthew", "chapter": 6, "verse": 3, "text": "But when thou doest alms, let not thy left hand know what thy right hand doeth:", "collection": "New Testament"},
        {"book": "Mark", "chapter": 16, "verse": 19, "text": "So then after the Lord had spoken unto them, he was received up into heaven, and sat on the right hand of God.", "collection": "New Testament"},
        {"book": "1 Nephi", "chapter": 20, "verse": 13, "text": "Mine hand hath also laid the foundation of the earth, and my right hand hath spanned the heavens. When I call unto them, they stand up together.", "collection": "Book of Mormon"},
        {"book": "Alma", "chapter": 5, "verse": 58, "text": "Will ye not now return unto me, and repent of your sins, and be converted, that I may heal you? Yea, verily I say unto you, if ye will come unto me ye shall have eternal life. Behold, mine arm of mercy is extended towards you, and whosoever will come, him will I receive; and blessed are those who come unto me.", "collection": "Book of Mormon"},
        {"book": "Doctrine and Covenants", "chapter": 27, "verse": 18, "text": "Wherefore, take unto you the whole armor of God, that ye may be able to withstand in the evil day, and having done all, to stand.", "collection": "Doctrine and Covenants"}
    ]
    
    # Clear existing data
    db.session.query(Scripture).delete()
    
    # Add new scriptures
    for scripture_data in scriptures_data:
        scripture = Scripture(**scripture_data)
        db.session.add(scripture)
    
    # Commit all changes
    db.session.commit()
    
    print(f"Successfully populated database with {len(scriptures_data)} scripture verses")
    return len(scriptures_data)

if __name__ == "__main__":
    from src.main import app
    with app.app_context():
        populate_scriptures()

